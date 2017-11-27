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

def load_query (metodo,tipo,anio1,anio2):
    if tipo =="mensual":
        if anio1 == anio2 and anio1!="":
            txt = open(r".\sql\%s" % (dict_metodos_mensuales[str(metodo)]), "r")
            array_txt = (" ").join([x.replace("\n", "") for x in txt.readlines()])
            ctable_expresion = '''%s''' % (array_txt)
            ctable_expresion=ctable_expresion + """ and anio = {}""".format(anio1)
        elif anio1 != anio2:
            con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                    port="5432")
            con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor1 = con1.cursor()
            try :
                cursor1.execute("DROP table tmp_query_mensual")
            except:
                pass
            txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
            ce='''CREATE table tmp_query_mensual as ('''
            ctable_e= '''%s''' % (txt.read())
            print ce+ctable_e+")"
            cursor1.execute(ce+ctable_e+")")
            ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
            ctable_expresion=ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1,anio2)
        elif anio1 == anio2 and anio1=="":
            txt = open(r".\sql\%s" % (dict_metodos_mensuales[str(metodo)]), "r")
            array_txt = (" ").join([x.replace("\n", "") for x in txt.readlines()])
            ctable_expresion = '''%s''' % (array_txt)

    if tipo =="decadal":
        # aqui viene el decadal
        pass
    txt.close()
    #txt1.close()
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
    print cmd
    process = os.system(cmd)

#load_query("Thornthwaite","")

#export_pg_table(r"C:\export_data\\", 'tmp_evot_gl', 'localhost', 'postgres', 'postgres', 'evot', gl.format(2000))