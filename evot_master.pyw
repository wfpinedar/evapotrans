# -*- coding: utf-8 -*-
import sys
from evotui.evotgui import *
from evapot.query_maker import *
from evapot.query_maker_all import *
from evapot.export_2_excel import *
from evapot.export_rast import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.importtab)
        self.ui.mdiArea.addSubWindow(self.ui.eporttab)
        self.ui.mdiArea.addSubWindow(self.ui.conex)
        print self.ui.mdiArea.subWindowList()[0].windowTitle()
        QtCore.QObject.connect(self.ui.bNext, QtCore.SIGNAL('clicked()'), self.displayNext)
        QtCore.QObject.connect(self.ui.bPrev, QtCore.SIGNAL('clicked()'),self.displayPrevious)
        QtCore.QObject.connect(self.ui.bClose, QtCore.SIGNAL('clicked()'), self.closeAll)
        QtCore.QObject.connect(self.ui.bCas, QtCore.SIGNAL('clicked()'), self.cascadeArrage)
        QtCore.QObject.connect(self.ui.bMos, QtCore.SIGNAL('clicked()'), self.tileArrage)
        QtCore.QObject.connect(self.ui.bSub, QtCore.SIGNAL('clicked()'), self.SubWindowView)
        QtCore.QObject.connect(self.ui.bPes, QtCore.SIGNAL('clicked()'), self.TabbedView)
        self.connect(self.ui.importtab, QtCore.SIGNAL('triggered()'), self.displayNext)
        self.connect(self.ui.eporttab, QtCore.SIGNAL('triggered()'), self.displayPrevious)
        self.connect(self.ui.conex, QtCore.SIGNAL('triggered()'), self.displayPrevious)
        QtCore.QObject.connect(self.ui.bTest, QtCore.SIGNAL('clicked()'), self.testConnect)
        self.ui.lDb.setText("evot")
        self.ui.lUsr.setText("postgres")
        self.ui.lPass.setText("postgres")
        self.ui.lHost.setText("localhost")
        self.ui.lPort.setText("5432")
        self.connect(self.ui.bRuta, QtCore.SIGNAL('clicked()'), self.onInputFileButtonClicked)
        QtCore.QObject.connect(self.ui.bExport, QtCore.SIGNAL('clicked()'), self.dataExport)
        self.ui.cTipo.currentIndexChanged.connect(self.change_type_method)
        self.ui.cPeriodicidad.currentIndexChanged.connect(self.change_type_period)
        self.ui.cMetho.addItems(["Blaney-Criddle", "Christiansen", "Hargreaves", "Linacre", "Penman-Monteith",
                                 "Thornthwaite", "Turc"])
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[1])

    def change_type_period(self):
        self.ui.cMetho.clear()
        if self.ui.cPeriodicidad.currentText() == 'Mensual':
            self.ui.cMetho.addItems(["Blaney-Criddle", "Christiansen", "Hargreaves", "Linacre", "Penman-Monteith",
                                     "Thornthwaite", "Turc"])
        else:
            self.ui.cMetho.addItems(["Penman-Monteith"])


    def change_type_method(self):
        self.ui.cMetho.clear()
        if self.ui.cTipo.currentText()=='Resultado':
            self.ui.label_8.setText("Metodo")
            self.ui.cMetho.addItems(["Blaney-Criddle", "Christiansen", "Hargreaves", "Linacre", "Penman-Monteith",
                                     "Thornthwaite", "Turc"])
        else:
            self.ui.label_8.setText("Variable")
            self.ui.cMetho.addItems(["Brillo Solar", "Evaporacion", "Humedad Relativa", "Temp.Max", "Temp.Media",
                                     "Temp.Min", "Velocidad"])

    def alert(self, msg, icon=QtGui.QMessageBox.Warning):
        d = QtGui.QMessageBox()
        d.setWindowTitle('Warning valid options')
        d.setText(msg)
        d.setIcon(icon)
        d.exec_()

    def shpExport(self):
        export_pg_table(self.ui.lRuta.text(), self.ui.lShpName.text(),
                        self.ui.lHost.text(), self.ui.lUsr.text(), self.ui.lPass.text(), self.ui.lDb.text(),
                        load_query(self.ui.cTipo.currentText(),self.ui.cAgrup.currentText(),self.ui.cMetho.currentText(),self.ui.cPeriodicidad.currentText(), self.ui.anio1.text(), self.ui.anio2.text()))


    def excExport(self):
        make_excel(get_table(self.ui.lDb.text(), load_query(self.ui.cMetho.currentText(),"mensual",
                   self.ui.anio1.text(), self.ui.anio2.text())), self.ui.lRuta.text(), self.ui.lShpName.text())

    def rasExport(self):
        make_rast(self.ui.lShpName.text(), self.ui.lRuta.text())

    def dataExport(self):
        if self.ui.cShp.isChecked() and self.ui.cExcl.isChecked() and self.ui.cExcl_2.isChecked():
            self.shpExport()
            self.excExport()
            self.rasExport()
        elif self.ui.cShp.isChecked() and self.ui.cExcl.isChecked():
            self.shpExport()
            self.excExport()
        elif self.ui.cShp.isChecked() and self.ui.cExcl_2.isChecked():
            self.shpExport()
            self.rasExport()
        elif self.ui.cShp.isChecked() and self.ui.cExcl.isChecked()is not True:
            self.shpExport()
        elif self.ui.cShp.isChecked() is not True and self.ui.cExcl.isChecked():
            self.excExport()
        else:
            self.alert("Seleccione el formato de salida del Archivo")

        #self.ui.lRuta.clear()
        #self.ui.lShpName.clear()

    def onInputFileButtonClicked(self):
        self.ui.lRuta.setText(QtGui.QFileDialog.getExistingDirectory(None, 'Open Folder'))

    def testConnect(self):
        try:
            con = psycopg2.connect(database=self.ui.lDb.text(),
                                   user=self.ui.lUsr.text(),
                                   password=self.ui.lPass.text(),
                                   host=self.ui.lHost.text(),
                                   port=self.ui.lPort.text())
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cursor = con.cursor()
            cursor.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'evot'")
            not_exists_row = cursor.fetchone()
            not_exists = not_exists_row[0]
        except:
            not_exists=True
        if not_exists:
            self.ui.lSuccess.setText("Conexion no Funciona")
        else:
            self.ui.lSuccess.setText("Conexion Realizada")

    def displayNext(self):
        self.ui.mdiArea.activateNextSubWindow()

    def displayPrevious(self):
        self.ui.mdiArea.activatePreviousSubWindow()

    def closeAll(self):
        self.ui.mdiArea.closeAllSubWindows()

    def cascadeArrage(self):
        self.ui.mdiArea.cascadeSubWindows()

    def tileArrage(self):
        self.ui.mdiArea.tileSubWindows()

    def SubWindowView(self):
        self.ui.mdiArea.setViewMode(0)

    def TabbedView(self):
        self.ui.mdiArea.setViewMode(1)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
