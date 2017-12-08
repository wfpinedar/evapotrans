# -*- coding: utf-8 -*-
import sys
from evotui.evotgui import *
from evapot.query_maker import *
from evapot.query_maker_all import *
from evapot.export_2_excel import *
from evapot.export_rast import *
from evapot.create_load_bd import *
from evapot.load_formulas import *
from evapot .add_geoColum import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.importtab)
        self.ui.mdiArea.addSubWindow(self.ui.eporttab)
        print self.ui.mdiArea.subWindowList()[0].windowTitle()
        self.ui.lDb.setText("evot")
        self.ui.lUsr.setText("postgres")
        self.ui.lPass.setText("postgres")
        self.ui.lHost.setText("localhost")
        self.ui.lPort.setText("5432")

        self.ui.lRuta_impfile.setEnabled(False)
        self.ui.lRuta_foldsalid.setEnabled(False)
        self.ui.bRuta_imp.setEnabled(False)
        self.ui.bRuta_exp.setEnabled(False)

        self.connect(self.ui.bRuta, QtCore.SIGNAL('clicked()'), self.onInputFileButtonClicked)
        self.connect(self.ui.bRuta_var, QtCore.SIGNAL('clicked()'), self.abir_archivo)
        QtCore.QObject.connect(self.ui.bExport, QtCore.SIGNAL('clicked()'), self.dataExport)
        self.ui.cTipo.currentIndexChanged.connect(self.change_type_period)
        self.ui.cAgrup.currentIndexChanged.connect(self.change_type_period)
        QtCore.QObject.connect(self.ui.bBd, QtCore.SIGNAL('clicked()'), self.bd_options)
        QtCore.QObject.connect(self.ui.bCvar, QtCore.SIGNAL('clicked()'), self.data_options)
        self.ui.cPeriodicidad.currentIndexChanged.connect(self.change_type_period)
        self.ui.cBdop.currentIndexChanged.connect(self.bd_options_changer)
        self.ui.cMetho.addItems(["Blaney-Criddle", "Christiansen", "Hargreaves", "Linacre", "Penman-Monteith",
                                 "Thornthwaite", "Turc"])

        self.ui.cVariable.addItems(["Brillo Solar", "Estaciones", "Evaporacion", "Humedad Relativa", "Punto de Rocio",
                                  "Radiacion Extraterrestre","Temperatura Maxima",
                                 "Temperatura Minima", "Temperatura Media", "Velocidad del Viento"])
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[1])

    def lform(self,db,us,host,port,pas):
        add_formulas(r".\sql\formulas_evot_pm.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_tw.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_cht.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_bc.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_gl.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_ln.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_tur.txt",db,us,host,port,pas)
        add_formulas(r".\sql\formulas_evot_har.txt",db,us,host,port,pas)

    def change_type_period(self):
        self.ui.cMetho.clear()

        if self.ui.cPeriodicidad.currentText() == 'Mensual'and self.ui.cTipo.currentText()=='Resultado':
            self.ui.label_8.setText("Metodo")
            self.ui.cMetho.addItems(["Blaney-Criddle", "Christiansen", "Hargreaves", "Linacre", "Penman-Monteith",
                                     "Thornthwaite", "Turc"])
        elif self.ui.cPeriodicidad.currentText() == 'Mensual'and self.ui.cTipo.currentText()=='Variable':
            self.ui.label_8.setText("Variable")
            self.ui.cMetho.addItems(["Brillo Solar", "Evaporacion", "Humedad Relativa", "Temp.Max", "Temp.Media",
                                     "Temp.Min", "Velocidad"])
        elif self.ui.cPeriodicidad.currentText() == 'Decadal'and self.ui.cTipo.currentText()=='Resultado':
            self.ui.label_8.setText("Metodo")
            self.ui.cMetho.addItems(["Penman-Monteith"])

        elif self.ui.cPeriodicidad.currentText() == 'Decadal'and self.ui.cTipo.currentText()=='Variable':
            self.ui.label_8.setText("Variable")
            self.ui.cMetho.addItems(["Brillo Solar", "Evaporacion", "Humedad Relativa", "Temp.Max", "Temp.Media",
                                     "Temp.Min", "Velocidad"])
    def bd_options_changer(self):
        opcion_bd=str(self.ui.cBdop.currentText())

        if opcion_bd =='Importar Base de Datos':
            self.ui.lRuta_impfile.setEnabled(True)
            self.ui.lRuta_foldsalid.setEnabled(False)
            self.ui.bRuta_imp.setEnabled(True)
            self.ui.bRuta_exp.setEnabled(False)
        elif opcion_bd =='Exportar Base de Datos':
            self.ui.lRuta_impfile.setEnabled(False)
            self.ui.lRuta_foldsalid.setEnabled(True)
            self.ui.bRuta_imp.setEnabled(False)
            self.ui.bRuta_exp.setEnabled(True)

        else:
            self.ui.lRuta_impfile.setEnabled(False)
            self.ui.lRuta_foldsalid.setEnabled(False)
            self.ui.bRuta_imp.setEnabled(False)
            self.ui.bRuta_exp.setEnabled(False)


    def bd_options(self):
        opcion_bd = str(self.ui.cBdop.currentText())
        usr=str(self.ui.lUsr.text())
        pas=str(self.ui.lPass.text())
        port=str(self.ui.lPort.text())
        host=str(self.ui.lHost.text())
        bd=str(self.ui.lDb.text())

        if opcion_bd == 'Verificar Base de Datos':
            self.testConnect()

        if opcion_bd ==  "Crear Base de Datos":
            build_db(bd, usr, host, port, pas)
            self.lform(bd, usr, host, port, pas)
            self.alert("la Base fue creada con exito")
            self.testConnect()


    def data_options(self):
        opcion_bd = str(self.ui.cVariable.currentText())
        usr = str(self.ui.lUsr.text())
        pas = str(self.ui.lPass.text())
        port = str(self.ui.lPort.text())
        host = str(self.ui.lHost.text())
        bd = str(self.ui.lDb.text())

        if opcion_bd == 'Verificar Base de Datos':
            self.testConnect()

        if opcion_bd == "Crear Base de Datos":
            build_db(bd, usr, host, port, pas)
            self.lform(bd, usr, host, port, pas)
            self.alert("la Base fue creada con exito")
            self.testConnect()

        if opcion_bd in ["Evaporacion", "Brillo Solar", "Humedad Relativa", "Temperatura Maxima",
                         "Temperatura Minima",
                         "Temperatura Media", "Velocidad del Viento"]:

            load_variable(r"%s" % (str(self.ui.lRuta_var.text())), bd,'variable',usr, host, port, pas)
            self.alert("Archivo de %s cargado con exito"%(opcion_bd))

        if opcion_bd == "Estaciones":
            load_station(r"%s" % (str(self.ui.lRuta_var.text())), bd, "estacion")
            cal_geoColum(bd, "estacion", usr, host, port, pas)
            self.alert("Archivo de estaciones cargado con exito")

        if opcion_bd in ["Punto de Rocio", "Radiacion Extraterrestre"]:
            if opcion_bd =="Radiacion Extraterrestre":
                load_rad_har(r"%s" % (str(self.ui.lRuta_var.text())), bd,'rad_extra_har',usr, host, port, pas)
                self.alert("Archivo de Radiacion Extraterrestre cargado con exito")
            else:
                load_rad_har(r"%s" % (str(self.ui.lRuta_var.text())), bd, 'p_rocio_ln', usr, host, port, pas)
                self.alert("Archivo de Punto de Rocio cargado con exito")



    def alert(self, msg, icon=QtGui.QMessageBox.Warning):
        d = QtGui.QMessageBox()
        d.setWindowTitle('Mensaje de Alerta')
        d.setText(msg)
        d.setIcon(icon)
        d.exec_()

    def shpExport(self):
        #get_table_shp
        export_pg_table(self.ui.lRuta.text(), self.ui.lShpName.text(),
                        self.ui.lHost.text(), self.ui.lUsr.text(), self.ui.lPass.text(), self.ui.lDb.text(),
                        load_query(self.ui.cTipo.currentText(),self.ui.cAgrup.currentText(),self.ui.cMetho.currentText(),
                                   self.ui.cPeriodicidad.currentText(), self.ui.anio1.text(), self.ui.anio2.text()))


    def excExport(self):
        make_excel(get_table(self.ui.lDb.text(), load_query(self.ui.cTipo.currentText(),self.ui.cAgrup.currentText(),self.ui.cMetho.currentText(),
                                   self.ui.cPeriodicidad.currentText(), self.ui.anio1.text(), self.ui.anio2.text())),
                                   self.ui.lRuta.text(), self.ui.lShpName.text())

    def rasExport(self):
        make_rast(self.ui.lShpName.text(), self.ui.lRuta.text(), self.ui.cPeriodicidad.currentText())

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

    def abir_archivo(self):
        self.ui.lRuta_var.setText(QtGui.QFileDialog.getOpenFileNameAndFilter(self,"Abrir Archivo", "",'', '*.csv')[0])

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
            self.ui.chBbd.setChecked(False)
            self.alert("La base de datos no Existe")
        else:
            self.ui.chBbd.setChecked(True)
            self.alert("La base de datos Existe")

    def test_data(self,opcion):
        pass



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
