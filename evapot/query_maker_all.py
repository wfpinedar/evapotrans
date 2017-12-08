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

dict_variables_mensuales={
"Brillo Solar":"BS",
"Evaporacion":"EV",
"Humedad Relativa":"HR",
"Temp.Max":"TMX",
"Temp.Media":"TMD",
"Temp.Min":"TMN",
"Velocidad":"VD"}

dict_variables_menusuales_promedio={"Brillo Solar":"", "Evaporacion":"", "Humedad Relativa":"", "Temp.Max":"", "Temp.Media":"",
                                     "Temp.Min":"", "Velocidad":""}



def load_query (tipo,agrupacion,metodo,periodo,anio1,anio2):
    if tipo=="Resultado":
            if anio1!="" and anio2=="":
                con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                        port="5432")
                con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor1 = con1.cursor()
                try :
                    cursor1.execute("DROP table tmp_query_mensual")
                    cursor1.execute("DROP table tmp_query_prom")
                    cursor1.execute("DROP table tmp_query_prom1")
                except:
                    pass

                if periodo == "Mensual":
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)
                    else:# promedio
                        txt = open(r".\sql\%s" % (dict_metodos_mensuales[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)
                        cursor1.execute('''CREATE table tmp_query_prom as ('''+ctable_expresion+")")

                        txt = open(r".\sql\%s" % (dict_metodos_mensuales_promedio[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_prom1 as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                        ctable_expresion = ctable_expresion
                else:
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_decadales[str(metodo)]),"r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)
                    else: # promedio
                        txt = open(r".\sql\%s" % (dict_metodos_decadales[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)
                        cursor1.execute('''CREATE table tmp_query_prom as (''' + ctable_expresion + ")")

                        txt = open(r".\sql\%s" % (dict_metodos_decadales_promedio[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_prom1 as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                        ctable_expresion = ctable_expresion

            elif anio2!="" and anio1!="":
                con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                        port="5432")
                con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor1 = con1.cursor()
                try :
                    cursor1.execute("DROP table tmp_query_mensual")
                    cursor1.execute("DROP table tmp_query_prom")
                    cursor1.execute("DROP table tmp_query_prom1")
                except:
                    pass
                if periodo == "Mensual":
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1, anio2)
                    else:# promedio
                        txt = open(r".\sql\%s" % (dict_metodos_mensuales[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1,anio2)
                        cursor1.execute('''CREATE table tmp_query_prom as ('''+ctable_expresion+")")

                        txt = open(r".\sql\%s" % (dict_metodos_mensuales_promedio[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_prom1 as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                        ctable_expresion = ctable_expresion
                else:
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_decadales[str(metodo)]),"r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1, anio2)
                    else: # promedio
                        txt = open(r".\sql\%s" % (dict_metodos_decadales[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1, anio2)
                        cursor1.execute('''CREATE table tmp_query_prom as (''' + ctable_expresion + ")")

                        txt = open(r".\sql\%s" % (dict_metodos_decadales_promedio[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_prom1 as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                        ctable_expresion = ctable_expresion

            elif anio2 == "" and anio1 == "":
                con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                        port="5432")
                con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor1 = con1.cursor()
                try:
                    cursor1.execute("DROP table tmp_query_mensual")
                    cursor1.execute("DROP table tmp_query_prom")
                    cursor1.execute("DROP table tmp_query_prom1")
                except:
                    pass
                if periodo == "Mensual":
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_mensuales[str(metodo)]),"r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion
                    else:# promedio
                        txt = open(r".\sql\%s" % (dict_metodos_mensuales[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion
                        cursor1.execute('''CREATE table tmp_query_prom as ('''+ctable_expresion+")")

                        txt = open(r".\sql\%s" % (dict_metodos_mensuales_promedio[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_prom1 as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                        ctable_expresion = ctable_expresion
                else:
                    if agrupacion == "Normal":
                        txt  = open(r".\sql\%s"%(dict_metodos_decadales[str(metodo)]),"r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion
                    else: # promedio
                        txt = open(r".\sql\%s" % (dict_metodos_decadales[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_mensual as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                        ctable_expresion = ctable_expresion
                        cursor1.execute('''CREATE table tmp_query_prom as (''' + ctable_expresion + ")")

                        txt = open(r".\sql\%s" % (dict_metodos_decadales_promedio[str(metodo)]), "r")
                        ce = '''CREATE table tmp_query_prom1 as ('''
                        ctable_e = '''%s''' % (txt.read())
                        cursor1.execute(ce + ctable_e + ")")
                        ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                        ctable_expresion = ctable_expresion
    else:############################################### VARIABLES ########################################################################
        if anio1 != "" and anio2 == "":
            con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                    port="5432")
            con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor1 = con1.cursor()
            try:
                cursor1.execute("DROP table tmp_query_mensual")
                cursor1.execute("DROP table tmp_query_prom")
                cursor1.execute("DROP table tmp_query_prom1")
            except:
                pass

            if periodo == "Mensual":
                if agrupacion == "Normal":
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e =ctable_e.replace("&&&",dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)
                else:  # promedio
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e =ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)

                    txt = open(r".\sql\%s" % ("consulta_variable_mensual_promedio.txt"), "r")
                    ce = '''CREATE table tmp_query_prom1 as ('''
                    ctable_e = '''%s''' % (txt.read())
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                    ctable_expresion = ctable_expresion
            else:# decadal
                if agrupacion == "Normal" or agrupacion == "Promedio":
                    # txt = open(r".\sql\%s" % ("consulta_variable_decadal.txt"), "r")
                    # ce = '''CREATE table tmp_query_mensual as ('''
                    # ctable_e = '''%s''' % (txt.read())
                    # ctable_e = ce + ctable_e +")"
                    # ctable_e= ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    # cursor1.execute(ctable_e)
                    # ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    # ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion + """ where anio = {}""".format(anio1)

                    txt = open(r".\sql\%s" % ("consulta_variable_mensual_promedio.txt"), "r")
                    ce = '''CREATE table tmp_query_prom1 as ('''
                    ctable_e = '''%s''' % (txt.read())
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                    ctable_expresion = ctable_expresion

        elif anio2 != "" and anio1 != "":
            con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                    port="5432")
            con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor1 = con1.cursor()
            try:
                cursor1.execute("DROP table tmp_query_mensual")
                cursor1.execute("DROP table tmp_query_prom")
                cursor1.execute("DROP table tmp_query_prom1")
            except:
                pass

            if periodo == "Mensual":
                if agrupacion == "Normal":
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion +""" where anio >= {} and anio <=  {}""".format(anio1, anio2)
                else:  # promedio
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1, anio2)

                    txt = open(r".\sql\%s" % ("consulta_variable_mensual_promedio.txt"), "r")
                    ce = '''CREATE table tmp_query_prom1 as ('''
                    ctable_e = '''%s''' % (txt.read())
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                    ctable_expresion = ctable_expresion
            else:  # decadal
                if agrupacion == "Normal" or agrupacion == "Promedio":
                    txt = open(r".\sql\%s" % ("consulta_variable_decadal.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ce + ctable_e + ")"
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ctable_e)
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion + """ where anio >= {} and anio <=  {}""".format(anio1, anio2)

        elif anio2 == "" and anio1 == "":
            con1 = psycopg2.connect(database="evot", user="postgres", password="postgres", host="localhost",
                                    port="5432")
            con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor1 = con1.cursor()
            try:
                cursor1.execute("DROP table tmp_query_mensual")
                cursor1.execute("DROP table tmp_query_prom")
                cursor1.execute("DROP table tmp_query_prom1")
            except:
                pass

            if periodo == "Mensual":
                if agrupacion == "Normal":
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion
                else:  # promedio
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion

                    txt = open(r".\sql\%s" % ("consulta_variable_mensual_promedio.txt"), "r")
                    ce = '''CREATE table tmp_query_prom1 as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                    ctable_expresion = ctable_expresion
            else:  # decadal
                if agrupacion == "Normal" or agrupacion == "Promedio":
                    # txt = open(r".\sql\%s" % ("consulta_variable_decadal.txt"), "r")
                    # ce = '''CREATE table tmp_query_mensual as ('''
                    # ctable_e = '''%s''' % (txt.read())
                    # ctable_e = ce + ctable_e + ")"
                    # ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    # cursor1.execute(ctable_e)
                    # ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    # ctable_expresion = ctable_expresion
                    txt = open(r".\sql\%s" % ("consulta_variable_mensual.txt"), "r")
                    ce = '''CREATE table tmp_query_mensual as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_mensual ")
                    ctable_expresion = ctable_expresion

                    txt = open(r".\sql\%s" % ("consulta_variable_mensual_promedio.txt"), "r")
                    ce = '''CREATE table tmp_query_prom1 as ('''
                    ctable_e = '''%s''' % (txt.read())
                    ctable_e = ctable_e.replace("&&&", dict_variables_mensuales[str(metodo)])
                    cursor1.execute(ce + ctable_e + ")")
                    ctable_expresion = '''%s''' % ("select * from tmp_query_prom1 ")
                    ctable_expresion = ctable_expresion

    txt.close()

    return ctable_expresion



def export_pg_table(export_path, pgtable_name, host, username, password, db, agrupacion,periodo,tipo,pg_sql_select):
    ruta_shapes= export_path + "\%s_shapes" % (pgtable_name)
    try:
        os.stat(ruta_shapes)
    except:
        os.mkdir(ruta_shapes)

    if agrupacion == "Promedio" and periodo == "Decadal" and tipo=="Resultado":

        for x in xrange(36):
            campos = '''codigo ,tipo ,clase ,cat ,nombre ,municipio ,corriente ,departamento ,altitud , cod_dep ,cod_muni ,longitud ,latitud ,estado ,geom ,d%s'''%(x+1)
            pg_sql_select='''select %s as d%s from tmp_query_prom1 where d%s > 0'''%(campos,x+1,x+1)
            print "Exporting shapefile ..."
            cmd = '''pgsql2shp -f {export_path}\{pgtable_name}.shp -h {host} -u {username} -P {password} {db} "{pg_sql_select}"'''.format(
                pgtable_name=pgtable_name+"_d%s"%(x+1), export_path=ruta_shapes, host=host, username=username, db=db,
                password=password,
                pg_sql_select=pg_sql_select)
            process = os.system(cmd)

    elif agrupacion == "Promedio" and periodo == "Decadal" and tipo == "Variable":
        pass
