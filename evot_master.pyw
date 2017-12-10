# -*- coding: utf-8 -*-
import sys
from evotui.evotgui import *
from evapot.query_maker import *
from evapot.query_maker_all import *
from evapot.export_2_excel import *
from evapot.export_rast import *
from evapot.create_load_bd import *
from evapot.load_formulas import *
from evapot.add_geoColum import *
from evapot.build_db import bkp_db
from evapot.build_db import res_db
from evapot.build_db import drop_db
from evapot.tmp_dec_pm import *
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.importtab)
        self.ui.mdiArea.addSubWindow(self.ui.eporttab)
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
        self.connect(self.ui.bRuta_exp, QtCore.SIGNAL('clicked()'), self.exportdir)
        self.connect(self.ui.bRuta_imp, QtCore.SIGNAL('clicked()'), self.importdir)
        self.connect(self.ui.bRuta_var, QtCore.SIGNAL('clicked()'), self.abir_archivo)
        QtCore.QObject.connect(self.ui.bExport, QtCore.SIGNAL('clicked()'), self.dataExport)
        self.ui.cTipo.currentIndexChanged.connect(self.change_type_period)
        self.ui.cAgrup.currentIndexChanged.connect(self.change_type_period)
        self.ui.cBvar.currentIndexChanged.connect(self.operacion_changer)
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

    def operacion_changer(self):
        opcion_oper = str(self.ui.cBvar.currentText())
        if opcion_oper=="Cargar Datos":
            self.ui.cVariable.setEnabled(True)
            self.ui.lRuta_var.setEnabled(True)
            self.ui.bRuta_var.setEnabled(True)
        elif opcion_oper=="Eliminar Datos" :
            self.ui.cVariable.setEnabled(True)
            self.ui.lRuta_var.setEnabled(False)
            self.ui.bRuta_var.setEnabled(False)
        elif opcion_oper == "Verificar Datos":
            self.ui.cVariable.setEnabled(False)
            self.ui.lRuta_var.setEnabled(False)
            self.ui.bRuta_var.setEnabled(False)

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

        if opcion_bd == "Exportar Base de Datos":
            try:
                bkp_db(usr, pas, host, self.ui.lRuta_foldsalid.text(), bd)
                self.alert("Base de datos Exportada OK!")
            except:
                self.alert("Base de datos Export NOT FOUND!!!")

        if opcion_bd == "Importar Base de Datos":
            try:
                res = res_db(usr, host, self.ui.lRuta_impfile.text(), bd, pas, port)
                self.alert("%s" %(res))
            except:
                self.alert("Base de datos Import NOT FOUND!!!")

        if opcion_bd == "Borrar Base de Datos":
            self.testConnect()
            if self.ui.chBbd.isChecked():
                #drop_db(bd, usr, host, port, pas)
                try:
                    drop_db(bd, usr, host, port, pas)
                    self.alert("Borrada base de datos %s  OK!!!"%bd)
                except:
                    self.alert("Base de datos Delete NOT FOUND!!!")
            else:
                self.alert("No existe la Base de datos.")



    def data_options(self):
        if self.ui.chBbd.isChecked():
            opcion_data= str(self.ui.cBvar.currentText())
            nombre_dato=str(self.ui.cVariable.currentText())
            usr = str(self.ui.lUsr.text())
            pas = str(self.ui.lPass.text())
            port = str(self.ui.lPort.text())
            host = str(self.ui.lHost.text())
            bd = str(self.ui.lDb.text())

            if opcion_data == 'Verificar Datos':
                self.test_data()

            if opcion_data == "Crear Base de Datos":
                build_db(bd, usr, host, port, pas)
                self.lform(bd, usr, host, port, pas)
                self.alert("la Base fue creada con exito")
                self.testConnect()

            if opcion_data == "Cargar Datos":
                if nombre_dato in ["Evaporacion", "Brillo Solar", "Humedad Relativa", "Temperatura Maxima",
                                 "Temperatura Minima",
                                 "Temperatura Media", "Velocidad del Viento"]:

                    load_variable(r"%s" % (str(self.ui.lRuta_var.text())), bd,'variable',usr, host, port, pas)
                    self.alert("Archivo de %s ha sido cargado con exito"%(nombre_dato))

                if nombre_dato == "Estaciones":
                    load_station(r"%s" % (str(self.ui.lRuta_var.text())), bd, "estacion")
                    cal_geoColum(bd, "estacion", usr, host, port, pas)
                    self.alert("Archivo de estaciones ha sido cargado con exito")

                if nombre_dato in ["Punto de Rocio", "Radiacion Extraterrestre"]:
                    if nombre_dato =="Radiacion Extraterrestre":
                        load_rad_har(r"%s" % (str(self.ui.lRuta_var.text())), bd,'rad_extra_har',usr, host, port, pas)
                        self.alert("Archivo de Radiacion Extraterrestre ha sido cargado con exito")
                    else:
                        load_rad_har(r"%s" % (str(self.ui.lRuta_var.text())), bd, 'p_rocio_ln', usr, host, port, pas)
                        self.alert("Archivo de Punto de Rocio ha sido cargado con exito")
                self.test_data()

            elif opcion_data == "Eliminar Datos":
                opcion=str(self.ui.cVariable.currentText())
                self.delete_data(opcion)

        else:
            self.alert("Por favor primero valide la existencia de la base de datos")

    def delete_data(self,opcion):
        dict_valores_datos = {
            "Brillo Solar": "BS",
            "Evaporacion": "EV",
            "Humedad Relativa": "HR",
            "Temperatura Maxima": "TMX",
            "Temperatura Media": "TMD",
            "Temperatura Minima": "TMN",
            "Velocidad del Viento": "VD"}


        con = psycopg2.connect(database=self.ui.lDb.text(),
                               user=self.ui.lUsr.text(),
                               password=self.ui.lPass.text(),
                               host=self.ui.lHost.text(),
                               port=self.ui.lPort.text())
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
        cursor = con.cursor()
        if opcion in ["Brillo Solar", "Evaporacion", "Humedad Relativa", "Temperatura Maxima",
                           "Temperatura Media", "Temperatura Minima", "Velocidad del Viento"]:
            cursor.execute("DELETE FROM variable WHERE variable = '%s'" % (dict_valores_datos[opcion]))
        elif opcion == "Estaciones":
            cursor.execute("TRUNCATE TABLE public.estacion")
        elif opcion == "Punto de Rocio":
            cursor.execute("TRUNCATE TABLE public.p_rocio_ln")
        elif opcion == "Radiacion Extraterrestre":
            cursor.execute("TRUNCATE TABLE public.rad_extra_har")

        self.alert("La Tabla %s ha sido borrada con exito"%(opcion))
        self.test_data()

    def aditional_tables(self):
        usr = str(self.ui.lUsr.text())
        pas = str(self.ui.lPass.text())
        port = str(self.ui.lPort.text())
        host = str(self.ui.lHost.text())
        bd = str(self.ui.lDb.text())

        con1 = psycopg2.connect(database=bd, user=usr, password=pas, host=host, port=port)
        con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor1 = con1.cursor()
        try:
            cursor1.execute("DROP prom_dec")
        except:
            pass
        try:
            cursor1.execute("DROP table prom_men")

        except:
            pass
        try:
            cursor1.execute("DROP table prom_anio")
        except:
            pass
        try:
            cursor1.execute("DROP table tmp_dec_pm")
        except:
            pass



    def alert(self, msg, icon=QtGui.QMessageBox.Warning):
        d = QtGui.QMessageBox()
        d.setWindowTitle('Mensaje de Alerta')
        d.setText(msg)
        d.setIcon(icon)
        d.exec_()

    def shpExport(self):
        usr = str(self.ui.lUsr.text())
        pas = str(self.ui.lPass.text())
        port = str(self.ui.lPort.text())
        host = str(self.ui.lHost.text())
        bd = str(self.ui.lDb.text())

        export_pg_table(self.ui.lRuta.text(), self.ui.lShpName.text(),
                        self.ui.lHost.text(), self.ui.lUsr.text(), self.ui.lPass.text(), self.ui.lDb.text(),
                        self.ui.cAgrup.currentText(),self.ui.cPeriodicidad.currentText(),self.ui.cTipo.currentText(),load_query(self.ui.cTipo.currentText(),self.ui.cAgrup.currentText(),self.ui.cMetho.currentText(),
                                   self.ui.cPeriodicidad.currentText(), self.ui.anio1.text(), self.ui.anio2.text(),bd,usr, host, port, pas))


    def excExport(self):
        usr = str(self.ui.lUsr.text())
        pas = str(self.ui.lPass.text())
        port = str(self.ui.lPort.text())
        host = str(self.ui.lHost.text())
        bd = str(self.ui.lDb.text())

        make_excel(get_table(self.ui.lDb.text(), load_query(self.ui.cTipo.currentText(),self.ui.cAgrup.currentText(),self.ui.cMetho.currentText(),
                                   self.ui.cPeriodicidad.currentText(), self.ui.anio1.text(), self.ui.anio2.text(),bd,usr, host, port, pas)),
                                   self.ui.lRuta.text(), self.ui.lShpName.text())

    def rasExport(self):
        make_rast(self.ui.lShpName.text(), self.ui.lRuta.text(), self.ui.cPeriodicidad.currentText(),self.ui.cTipo.currentText())

    def dataExport(self):
        usr = str(self.ui.lUsr.text())
        pas = str(self.ui.lPass.text())
        port = str(self.ui.lPort.text())
        host = str(self.ui.lHost.text())
        bd = str(self.ui.lDb.text())

        con1 = psycopg2.connect(database=bd, user=usr, password=pas, host=host, port=port)
        con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor1 = con1.cursor()

        if self.ui.cB_datos.isChecked():
            try:
                cursor1.execute("TRUNCATE table prom_dec")
            except:
                pass
            try:
                cursor1.execute("TRUNCATE table prom_men")

            except:
                pass
            try:
                cursor1.execute("DROP table tmp_dec_pm")
            except:
                pass
            try:
                cursor1.execute("TRUNCATE table prom_anio")
            except:
                pass
            # creando las tablas de promedios anuales mensuales y decadales
            txt = open(r".\sql\tablas_decadales_mensuales_anuales.txt", "r")
            ctable_e = '''%s''' % (txt.read())
            cursor1.execute(ctable_e)
            txt.close()
            tmp_prom_dec(usr,pas,port,host,bd) # creacion de la tabla tmp_dec_pm

            self.alert("Tablas auxiliares creadas con exito")




            if self.ui.cAgrup.currentText() == "Promedio" and self.ui.cPeriodicidad.currentText() == "Decadal" and self.ui.cTipo.currentText() == "Variable":
                self.alert("El Promedio Decadal para Variables es igual al mensual, por favor ejecute el mensual")

            else:

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
        else:
            self.alert("Por favor primero valide el cargue de los datos")
            #self.ui.lRuta.clear()
            #self.ui.lShpName.clear()

    def onInputFileButtonClicked(self):
        self.ui.lRuta.setText(QtGui.QFileDialog.getExistingDirectory(None, 'Open Folder'))

    def exportdir(self):
        self.ui.lRuta_foldsalid.setText(QtGui.QFileDialog.getExistingDirectory(self, 'Open Folder'))

    def importdir(self):
        self.ui.lRuta_impfile.setText(QtGui.QFileDialog.getOpenFileNameAndFilter(self, "Abrir Archivo", "", '', '*.bkp')[0])

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

    def test_data(self):
        if self.ui.chBbd.isChecked():
            dict_valores_datos = {
                "Brillo Solar": "BS",
                "Evaporacion": "EV",
                "Humedad Relativa": "HR",
                "Temperatura Maxima": "TMX",
                "Temperatura Media": "TMD",
                "Temperatura Minima": "TMN",
                "Velocidad del Viento": "VD"}

            dict_nombres_checks = {
                "Brillo Solar": "bs",
                "Evaporacion": "ev",
                "Humedad Relativa": "hr",
                "Temperatura Maxima": "tx",
                "Temperatura Media": "tm",
                "Temperatura Minima": "tn",
                "Velocidad del Viento": "ve",
                "Estaciones": "est",
                "Punto de Rocio": "pr",
                "Radiacion Extraterrestre": "rad"}
            for nombre_dato in ["Brillo Solar", "Estaciones", "Evaporacion", "Humedad Relativa", "Punto de Rocio",
                                "Radiacion Extraterrestre", "Temperatura Maxima",
                                "Temperatura Minima", "Temperatura Media", "Velocidad del Viento"]:
                try:
                    con = psycopg2.connect(database=self.ui.lDb.text(),
                                           user=self.ui.lUsr.text(),
                                           password=self.ui.lPass.text(),
                                           host=self.ui.lHost.text(),
                                           port=self.ui.lPort.text())
                    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
                    cursor = con.cursor()
                    if nombre_dato in ["Brillo Solar", "Evaporacion", "Humedad Relativa", "Temperatura Maxima",
                                       "Temperatura Media","Temperatura Minima","Velocidad del Viento"]:
                        cursor.execute("SELECT COUNT(*) = 0 FROM public.variable WHERE variable = '%s'" % (
                            dict_valores_datos[nombre_dato]))
                    elif nombre_dato == "Estaciones":
                        cursor.execute("SELECT COUNT(*) = 0 FROM public.estacion")
                    elif nombre_dato == "Punto de Rocio":
                        cursor.execute("SELECT COUNT(*) = 0 FROM public.p_rocio_ln")
                    elif nombre_dato == "Radiacion Extraterrestre":
                        cursor.execute("SELECT COUNT(*) = 0 FROM public.rad_extra_har")
                    not_exists_row = cursor.fetchone()
                    not_exists = not_exists_row[0]
                except:
                    not_exists = True
                if not_exists:
                    expr="self.ui.cB_%s.setChecked(False)"%(dict_nombres_checks[nombre_dato])
                    exec(expr)
                    # self.alert("Los datos de no %s estan cargados"%(nombre_dato))
                else:
                    expr = "self.ui.cB_%s.setChecked(True)" % (dict_nombres_checks[nombre_dato])
                    exec (expr)
                    # self.alert("Los datos de %s estan cargados" % (nombre_dato))
                if self.ui.cB_bs.isChecked() and self.ui.cB_ev.isChecked() and self.ui.cB_hr.isChecked() \
                    and self.ui.cB_tx.isChecked() and self.ui.cB_tn.isChecked() and self.ui.cB_tm.isChecked() \
                    and self.ui.cB_ve.isChecked() and self.ui.cB_est.isChecked() and self.ui.cB_pr.isChecked() \
                    and self.ui.cB_rad.isChecked():
                    self.ui.cB_datos.setChecked(True)
                else:
                    self.ui.cB_datos.setChecked(False)
            self.alert("Los datos han sido verificados")
        else:
            self.alert("Por favor primero valide la existencia de la base de datos")






if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
