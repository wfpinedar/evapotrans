# -*- coding: utf-8 -*-
import sys
from evotgui import *
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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
