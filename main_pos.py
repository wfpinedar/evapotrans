# -*- coding: utf-8 -*-
from evapot.build_db import build_db
from evapot.load_station import load_station
from evapot.load_variable import load_variable
from evapot.add_geoColum import add_geoColum
from evapot.export_2_excel import make_excel, get_table, get_var
from evapot.load_formulas import add_formulas
from evapot.load_rad_har import load_rad_har

def main():
    DB="evot"
##    build_db()
##    load_station(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\Estaciones\estaciones.csv",DB,"estacion_fix")
    load_rad_har(r"E:\DOCUMENTOS\TRABAJOS INDEPENDIENTES\PROYECTO_EVAPOTRANS\datos_demo\tabla_radiacion_har.csv",DB,"rad_extra_har")
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
##    add_formulas(r".\sql\formulas_eot_pm.txt")
##    add_formulas(r".\sql\formulas_eot_tw.txt")
##    add_formulas(r".\sql\formulas_eot_cht.txt")
##    add_formulas(r".\sql\formulas_evot_bc.txt")
##    add_formulas(r".\sql\formulas_evot_gl.txt")
if __name__ == '__main__':
    main()
