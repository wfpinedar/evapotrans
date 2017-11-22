# -*- coding: utf-8 -*-
import sys
from evotui.evotgui import *
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
        QtCore.QObject.connect(self.ui.bNext, QtCore.SIGNAL('clicked()'), self.displayNext)
        QtCore.QObject.connect(self.ui.bPrev, QtCore.SIGNAL('clicked()'),self.displayPrevious)
        QtCore.QObject.connect(self.ui.bClose, QtCore.SIGNAL('clicked()'), self.closeAll)
        QtCore.QObject.connect(self.ui.bCas, QtCore.SIGNAL('clicked()'), self.cascadeArrage)
        QtCore.QObject.connect(self.ui.bMos, QtCore.SIGNAL('clicked()'), self.tileArrage)
        QtCore.QObject.connect(self.ui.bSub, QtCore.SIGNAL('clicked()'), self.SubWindowView)
        QtCore.QObject.connect(self.ui.bPes, QtCore.SIGNAL('clicked()'), self.TabbedView)
        self.connect(self.ui.importtab, QtCore.SIGNAL('triggered()'),self.displayNext)
        self.connect(self.ui.eporttab, QtCore.SIGNAL('triggered()'), self.displayPrevious)
        self.connect(self.ui.conex, QtCore.SIGNAL('triggered()'), self.displayPrevious)
        QtCore.QObject.connect(self.ui.bTest, QtCore.SIGNAL('clicked()'), self.testConnect)
        self.ui.lDb.setText("evot")
        self.ui.lUsr.setText("postgres")
        self.ui.lPass.setText("postgres")
        self.ui.lHost.setText("localhost")
        self.ui.lPort.setText("5432")

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