# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


def add_geoColum(db, tabla):
    con = psycopg2.connect(database=db, user="postgres", password="postgres", host="localhost", port="5432")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    cursor.execute('''
    ALTER TABLE %s ADD COLUMN geom geometry(POINT,4326);
    UPDATE %s SET geom = ST_SetSRID(ST_MakePoint(%s,%s),4326);'''%(tabla,tabla,"longitud","latitud"))