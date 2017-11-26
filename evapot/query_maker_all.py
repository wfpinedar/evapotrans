# -*- coding: utf-8 -*-
import os
import psycopg2

ctable_expresion=""

dict_metodos_mensuales={
"Thornthwaite":"consulta_evot_mensual_%s.txt"%("tw"),
"Christiansen":"consulta_evot_mensual_%s.txt"%("cht"),
"Blaney-Criddle":"consulta_evot_mensual_%s.txt"%("bc"),
"Linacre":"consulta_evot_mensual_%s.txt"%("ln"),
"Turc":"consulta_evot_mensual_%s.txt"%("turc"),
"Hargreaves":"consulta_evot_mensual_%s.txt"%("har"),
"Penman Monteith":"consulta_evot_mensual_%s.txt"%("pm")
}

gl2=""" select * from ( \
tmp_evot_bc )  \
where anual >0 """

def load_query (metodo,tipo,anio1,anio2):
    if tipo =="mensual":
        if anio1 == anio2 and anio1!="":
            txt  = open(".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
            ctable_expresion='''%s'''%(txt.read())
            ctable_expresion=ctable_expresion + """ and anio = {}""".format(anio1)
        elif anio1 != anio2:
            txt  = open(".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
            ctable_expresion='''%s'''%(txt.read())
            ctable_expresion=ctable_expresion + """ and anio >= {} and anio <=  {}""".format(anio1,anio2)
        elif anio1 == anio2 and anio1=="":
            txt  = open(".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
            ctable_expresion='''%s'''%(txt.read())
            ctable_expresion=ctable_expresion + """ and anio >= {} and anio <=  {}""".format(anio1,anio2)

    if tipo =="decadal":
        # aqui viene el decadal
        pass
    #txt1=open(".\sql\%s"%("hey.txt"),"w")
    #txt1.write(ctable_expresion)
    txt.close()
    #txt1.close()
    return ctable_expresion


def query(anio, db="evot"):
    con = psycopg2.connect (database=db, user="postgres", password="postgres", host="localhost", port="5432")
    val = []
    with con:
        cursor = con.cursor()
        cursor.execute(ctable_expresion)
        rows = cursor.fetchall()
        for row in rows:
            val.append(list(row))
        for i in val:
            print i
    return val

def export_pg_table(export_path, pgtable_name, host, username, password, db, pg_sql_select):
    print "Exporting shapefile ..."
    cmd = '''pgsql2shp -f {export_path}\{pgtable_name}.shp -h {host} -u {username} -P {password} {db} "{pg_sql_select}"'''.format(
        pgtable_name=pgtable_name, export_path=export_path, host=host, username=username, db=db, password=password,
        pg_sql_select=pg_sql_select)
    print cmd
    process = os.system(cmd)

#load_query("Thornthwaite","")

#export_pg_table(r"C:\export_data\\", 'tmp_evot_gl', 'localhost', 'postgres', 'postgres', 'evot', gl.format(2000))