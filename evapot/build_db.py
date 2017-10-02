# -*- coding: utf-8 -*-
import psycopg2
import easygui
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

def build_db():
    cdat = easygui.multpasswordbox("Ingrese datos de conexión", "Connect",
                                      ("database", "user", "host", "port", "password"),
                                      ("postgres", "postgres", "localhost", "5432"))
    #con = psycopg2.connect (database = "postgres", user="postgres", password="postgres", host="localhost", port="5432")
    con = psycopg2.connect(database=cdat[0], user=cdat[1], password=cdat[4], host=cdat[2], port=cdat[3])
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
    ##    cursor.execute(open("schema.sql", "r").read())