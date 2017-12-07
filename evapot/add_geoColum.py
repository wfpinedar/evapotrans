# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


def add_geoColum(bd, tabla,usr, host, port, pas):
    con = psycopg2.connect(database=bd, user=usr, password=pas, host=host, port=port)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    cursor.execute('''
    ALTER TABLE %s ADD COLUMN geom geometry(POINT,4326);
    UPDATE %s SET geom = ST_SetSRID(ST_MakePoint(%s,%s),4326);'''%(tabla,tabla,"longitud","latitud"))

def cal_geoColum(bd, tabla,usr, host, port, pas):
    con = psycopg2.connect(database=bd, user=usr, password=pas, host=host, port=port)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    cursor.execute('''
    UPDATE %s SET geom = ST_SetSRID(ST_MakePoint(%s,%s),4326);'''%(tabla,"longitud","latitud"))
