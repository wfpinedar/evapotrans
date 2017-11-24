# -*- coding: utf-8 -*-
import os
import psycopg2

gl = """select * from ( \
Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,anio, \
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre, \
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual, \
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre, \
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual, \
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre, \
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end + \
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end + \
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end + \
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end + \
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end + \
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end + \
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end + \
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  + \
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end + \
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end + \
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end + \
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual \
from tmp_evot_gl \
where anio = '{}' \
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,anio) as tmp \
where anual > 0"""


def query(anio, db="evot", method='gl'):
    con = psycopg2.connect (database=db, user="postgres", password="postgres", host="localhost", port="5432")
    val = []
    if method == 'gl':
        with con:
            cursor = con.cursor()
            cursor.execute(gl.format(anio))
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

#export_pg_table(r"C:\export_data\\", 'tmp_evot_gl', 'localhost', 'postgres', 'postgres', 'evot', gl.format(2000))