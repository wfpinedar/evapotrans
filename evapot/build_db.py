# -*- coding: utf-8 -*-
import psycopg2
import easygui
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

def build_db(db,us,host,port,pas):

    con = psycopg2.connect(database="postgres", user=us, password=pas, host=host, port=port)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'evot'")
    not_exists_row = cursor.fetchone()
    not_exists = not_exists_row[0]
    if not_exists:
        cursor.execute('''CREATE DATABASE evot ;''')
    else:
        print "DB evot exist"
    ### conexion a Evot
    con1 = psycopg2.connect (database = "evot", user="postgres", password="postgres", host="localhost", port="5432")
    con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor1 = con1.cursor()
    cursor1.execute('''CREATE EXTENSION postgis ;''')
    ## create tables
    txt= open(".\sql\create_tables_post.txt","r")
    ctable_expresion='''%s'''%(txt.read())
    txt.close()
    cursor1.execute(ctable_expresion)

def drop_db():
    pass
    ##    cursor.execute(open("schema.sql", "r").read())