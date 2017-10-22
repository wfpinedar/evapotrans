# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


def load_variable(path, db, tabla):
    con = psycopg2.connect (database=db, user="postgres", password="postgres", host="localhost", port="5432")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    cursor.execute("COPY %s FROM '%s' DELIMITER ';' CSV HEADER encoding 'windows-1251';"%("tmp_variable",path))
    cursor.execute("INSERT INTO %s SELECT * FROM %s"%(tabla, "tmp_variable"))
    cursor.execute("truncate tmp_variable")