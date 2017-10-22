# -*- coding: utf-8 -*-
from evapot.build_db import build_db
from evapot.load_station import load_station
from evapot.load_variable import load_variable
from evapot.add_geoColum import add_geoColum
from evapot.export_2_excel import make_excel, get_table, get_var

def main():
    DB="evot"
    build_db()
    load_station(r"C:\datos_demo\Estaciones\estaciones.csv",DB,"estacion")
    add_geoColum(DB,"estacion")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\TEMPERATURA_MEDIA.csv",DB,"variable")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\TEMPERATURA_MINIMA.csv",DB,"variable")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\TEMPERATURA_MAXIMA.csv",DB,"variable")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\HUMEDAD.csv",DB,"variable")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\EVAPORACION.csv",DB,"variable")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\BRILLO_SOLAR.csv",DB,"variable")
    load_variable(r"C:\datos_demo\Variables\AJUSTADAS\VELOCIDAD.csv",DB,"variable")
    make_excel(DB, get_table(DB, "variable"))
    make_excel(DB, get_var(DB, "BS"))

if __name__ == '__main__':
    main()
