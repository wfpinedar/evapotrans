# -*- coding: utf-8 -*-
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
ctable_expresion=""

dict_metodos_mensuales={
"Thornthwaite":"consulta_evot_mensual_%s.txt"%("tw"),
"Christiansen":"consulta_evot_mensual_%s.txt"%("cht"),
"Blaney-Criddle":"consulta_evot_mensual_%s.txt"%("bc"),
"Linacre":"consulta_evot_mensual_%s.txt"%("ln"),
"Turc":"consulta_evot_mensual_%s.txt"%("turc"),
"Hargreaves":"consulta_evot_mensual_%s.txt"%("har"),
"Penman-Monteith":"consulta_evot_mensual_%s.txt"%("pm")
}

dict_metodos_mensuales_promedio={
"Thornthwaite":"consulta_evot_mensual_%s_prom.txt"%("tw"),
"Christiansen":"consulta_evot_mensual_%s_prom.txt"%("cht"),
"Blaney-Criddle":"consulta_evot_mensual_%s_prom.txt"%("bc"),
"Linacre":"consulta_evot_mensual_%s_prom.txt"%("ln"),
"Turc":"consulta_evot_mensual_%s_prom.txt"%("turc"),
"Hargreaves":"consulta_evot_mensual_%s_prom.txt"%("har"),
"Penman-Monteith":"consulta_evot_mensual_%s_prom.txt"%("pm")
}
dict_metodos_decadales={
"Penman-Monteith":"consulta_evot_decadal_pm_consecutivo.txt",
}
dict_metodos_decadales_promedio={
"Penman-Monteith":"consulta_evot_decadal_pm_consecutivo_prom.txt",
}


def load_query (tipo,agrupacion,metodo,periodo,anio1,anio2):
    if tipo=="Resultado":
            if anio1!="" and anio2=="":
                con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                        port="5432")
                con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor1 = con1.cursor()
                try :
                    cursor1.execute("DROP table tmp_query_mensual")
                except:
                    pass

                if periodo == "Mensual":
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
                    else:
                        txt = open(r".\sql\%s" % (dict_metodos_mensuales_promedio[str(metodo)]), "r")
                else:
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_decadales[str(metodo)]),"r")
                    else:
                        txt = open(r".\sql\%s" % (dict_metodos_decadales_promedio[str(metodo)]), "r")
                ce='''CREATE table tmp_query_mensual as ('''
                ctable_e= '''%s''' % (txt.read())
                cursor1.execute(ce+ctable_e+")")
                ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                ctable_expresion=ctable_expresion + """ where anio = {}""".format(anio1,anio2)

            elif anio2!="" and anio1!="":
                con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                        port="5432")
                con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor1 = con1.cursor()
                try :
                    cursor1.execute("DROP table tmp_query_mensual")
                except:
                    pass
                if periodo == "Mensual":
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
                    else:
                        txt = open(r".\sql\%s" % (dict_metodos_mensuales_promedio[str(metodo)]), "r")
                else:
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_decadales[str(metodo)]),"r")
                    else:
                        txt = open(r".\sql\%s" % (dict_metodos_decadales_promedio[str(metodo)]), "r")
                ce='''CREATE table tmp_query_mensual as ('''
                ctable_e= '''%s''' % (txt.read())
                cursor1.execute(ce+ctable_e+")")
                ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                ctable_expresion=ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1,anio2)

            elif anio2 == "" and anio1 == "":
                con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                        port="5432")
                con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor1 = con1.cursor()
                try:
                    cursor1.execute("DROP table tmp_query_mensual")
                except:
                    pass
                if periodo == "Mensual":
                    if agrupacion == "Normal":
                        print "1"
                        txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
                    else:
                        print "2"
                        txt = open(r".\sql\%s" % (dict_metodos_mensuales_promedio[str(metodo)]), "r")
                else:
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_decadales[str(metodo)]),"r")
                    else:
                        txt = open(r".\sql\%s" % (dict_metodos_decadales_promedio[str(metodo)]), "r")
                ce = '''CREATE table tmp_query_mensual as ('''
                ctable_e = '''%s''' % (txt.read())
                cursor1.execute(ce + ctable_e + ")")
                ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                ctable_expresion = ctable_expresion
    else:
        #aqui viene si es variable incial
        pass
    txt.close()
    return ctable_expresion


def query(db="evot"):
    con = psycopg2.connect (database=db, user="postgres", password="postgres", host="localhost", port="5432")
    val = []
    with con:
        cursor = con.cursor()
        cursor.execute("create table evot1_temp from "+ ctable_expresion)

def export_pg_table(export_path, pgtable_name, host, username, password, db, pg_sql_select):
    print "Exporting shapefile ..."
    cmd = '''pgsql2shp -f {export_path}\{pgtable_name}.shp -h {host} -u {username} -P {password} {db} "{pg_sql_select}"'''.format(
        pgtable_name=pgtable_name, export_path=export_path, host=host, username=username, db=db, password=password,
        pg_sql_select=pg_sql_select)
    #print cmd
    process = os.system(cmd)

#load_query("Thornthwaite","")

#export_pg_table(r"C:\export_data\\", 'tmp_evot_gl', 'localhost', 'postgres', 'postgres', 'evot', gl.format(2000))