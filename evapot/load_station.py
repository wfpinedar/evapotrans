# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

def load_station(path,db,usr,pas,host,port,tabla):
    con = psycopg2.connect (database = db, user=usr, password=pas, host=host, port=port)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    cursor.execute("COPY %s FROM '%s' DELIMITER ';' CSV HEADER encoding 'latin-1';"%("tmp_estacion",path))
    #iso 8859-1
    cursor.execute("INSERT INTO %s SELECT * FROM %s"%(tabla,"tmp_estacion"))
    cursor.execute("truncate tmp_estacion")