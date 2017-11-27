import easygui
import xlsxwriter
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


def get_var(db,var):
    con = psycopg2.connect(database=db, user="postgres", password="postgres", host="localhost", port="5432")
    val = []
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con:
        cur = con.cursor()
        cur.execute(str("select * from variable where variable=\'{0}\' ".format(var.encode('utf-8'))))
        rows = cur.fetchall()
        print len(rows)
        for row in rows:
            val.append(list(row))
    return val


def get_table(db, query):
    con = psycopg2.connect(database=db, user="postgres", password="postgres", host="localhost", port="5432")
    val = []
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con:
        cur = con.cursor()
        cur.execute(str(query))
        rows = cur.fetchall()
        val.append([n.name for n in cur.description])
        for row in rows:
            val.append(list(row))
    return val


def make_excel(table,export_path,pgtable_name):
    #save_file = easygui.filesavebox("Excel Estaciones", "Open File", '.xlsx',
    #                               filetypes=["*.xls", ["*.xlsx", "Excel 2010 files"]])
    save_file = "{export_path}\{pgtable_name}.xlsx".format(pgtable_name=pgtable_name, export_path=export_path)
    workbook = xlsxwriter.Workbook(r''+save_file)
    worksheet = workbook.add_worksheet()
    print
    for row,data in enumerate(table):
        worksheet.write_row(row,0,data)
    workbook.close()