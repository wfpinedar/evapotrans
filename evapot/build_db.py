# -*- coding: utf-8 -*-
import psycopg2
import os
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


def bkp_db(user,key,host,directorio,db):
    USER = user
    PASS = key
    HOST = host
    database_name = db
    BACKUP_DIR = directorio
    dumper = """pg_dump -U %s -Z 9 -f %s -F c %s  """

    os.putenv('PGPASSWORD', PASS)
    try:
        file_info = os.stat(file)
        msn = "Backup de datos existe. No se sobre escriben Backups"
    except:
        file_name = database_name + ".bkp"
        command = dumper % (USER, BACKUP_DIR + '\\' + file_name, database_name)
        print command
        os.system(command)


def res_db(user, host, file, db, key, port):
    USER = user
    HOST = host
    database_name = db
    RESTORE_FILE = file
    PASS = key
    con = psycopg2.connect(database="postgres", user=user, password=PASS, host=HOST, port=port)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'evot'")
    not_exists_row = cursor.fetchone()
    not_exists = not_exists_row[0]
    if not_exists:
        cursor.execute('''CREATE DATABASE evot ;''')
        dumper = """pg_restore --host %s -U %s --dbname %s --no-password  --verbose %s"""
        os.putenv('PGPASSWORD', PASS)
        file_name = database_name + ".bkp"
        command = dumper % (HOST, USER, database_name, RESTORE_FILE)
        print command
        os.system(command)
        res = "DB restaurada OK!!!"
    else:
        res = "ERROR: DB exist"
    return res
