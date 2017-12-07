# -*- coding: utf-8 -*-
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
from evapot.build_db import build_db
from evapot.load_station import load_station
from evapot.load_variable import load_variable
from evapot.add_geoColum import add_geoColum
from evapot.export_2_excel import make_excel, get_table, get_var
from evapot.load_formulas import add_formulas
from evapot.load_rad_har import load_rad_har


DB="evot"

def main(opcion,ruta):

    if str(opcion) =="Crear Base de Datos":
        build_db()

    if str(opcion) in ["Evaporacion","Brillo Solar","Humedad Relativa","Temperatura Maxima","Temperatura Minima",
                       "Temperatura Media", "Velocidad del Viento"]:

        pass

    if str(opcion) == "Estaciones":
        load_station(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\Estaciones\estaciones.csv",
                     DB, "estacion_fix")
        pass

    if str(opcion) in ["Punto de Rocio","Radiacion Extraterrestre"]:
        pass




#
#
##    load_station(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\Estaciones\estaciones.csv",DB,"estacion_fix")
##    load_rad_har(r'E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\ra_har.csv', DB, 'rad_extra_har')
# load_rad_har(r'E:\DOCUMENTOS\GitHub\evapotrans\datos_iniciales\punto_rocio_linacre.csv', DB, 'p_rocio_ln')
##    add_geoColum(DB,"estacion")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\TEMPERATURA_MEDIA.csv",DB,"variable")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\TEMPERATURA_MINIMA.csv",DB,"variable")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\TEMPERATURA_MAXIMA.csv",DB,"variable")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\HUMEDAD.csv",DB,"variable")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\EVAPORACION.csv",DB,"variable")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\BRILLO_SOLAR.csv",DB,"variable")
##    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\VELOCIDAD.csv",DB,"variable")
##    make_excel(DB, get_table(DB, "variable"))
##    make_excel(DB, get_var(DB, "BS"))

if __name__ == '__main__':
    main()
