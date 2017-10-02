# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kanoc
#
# Created:     30/09/2017
# Copyright:   (c) kanoc 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import xlrd
import sqlite3
#import easygui
from os.path import realpath


def build_db(path,name):
    conn = sqlite3.connect('%s\%s.gpkg'%(path,name))
    c = conn.cursor()
    conn.enable_load_extension(True)
    conn.execute("SELECT load_extension('mod_spatialite')")
    txt= open(".\sql\create_tables.txt","r")
    ctable_expresion='''%s'''%(txt.read())
    txt.close()
    c.executescript(ctable_expresion)

def load_estations(path,db):
    XLS_FILE = path
    ws = xlrd.open_workbook(r''+XLS_FILE).sheet_by_index(0)
    ROW_SPAN = (1, ws.nrows)
    COL_SPAN = (0, ws.ncols)
    exceldata = [[ws.cell_value(row, col)
                  for col in xrange(COL_SPAN[0], COL_SPAN[1])]
                 for row in xrange(ROW_SPAN[0], ROW_SPAN[1])]
    conn = sqlite3.connect(db)
    c = conn.cursor()
##    conn.enable_load_extension(True)
##    conn.execute("SELECT load_extension('mod_spatialite')")
    for row in exceldata:
        c.execute('INSERT INTO estacion VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
    conn.commit()
##    c.execute('''SELECT InitSpatialMetaData();''')
##    txt= open(".\sql\load_stations.txt","r")
##    lsatations_expresion='''%s'''%(txt.read())
##    txt.close()
##    c.executescript(lsatations_expresion)

def load_variable(path,db):
    XLS_FILE = path
    ws = xlrd.open_workbook(r''+XLS_FILE).sheet_by_index(0)
    ROW_SPAN = (1, ws.nrows)
    COL_SPAN = (0, ws.ncols)
    exceldata = [[ws.cell_value(row, col)
                  for col in xrange(COL_SPAN[0], COL_SPAN[1])]
                 for row in xrange(ROW_SPAN[0], ROW_SPAN[1])]
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for row in exceldata:
        c.execute('INSERT INTO variable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
    conn.commit()

def main():
    build_db(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\BD","Eto")
    DB=os.path.join(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\BD","Eto%s"%(".gpkg"))
    load_estations(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\Estaciones\estaciones.xls",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\BRILLO_SOLAR.xlsx",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\EVAPORACION.xlsx",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\HUMEDAD.xlsx",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\TEMPERATURA_MAXIMA.xlsx",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\TEMPERATURA_MEDIA.xlsx",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\TEMPERATURA_MINIMA.xlsx",DB)
    load_variable(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\variables\AJUSTADAS\VELOCIDAD.xlsx",DB)


if __name__ == '__main__':
    main()
