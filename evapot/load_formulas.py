# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


def add_formulas(path):
    con1 = psycopg2.connect (database = "evot", user="postgres", password="postgres", host="localhost", port="5432")
    con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor1 = con1.cursor()
    ## loan pm
    txt= open(path,"r")
    ctable_expresion='''%s'''%(txt.read())
    txt.close()
##    print ctable_expresion
    cursor1.execute(ctable_expresion)

##    formulas_eot_tw.txt
