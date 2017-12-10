import easygui
import xlsxwriter
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE



def get_table(db,usr,pas,host,port, query):
    con = psycopg2.connect(database=db, user=usr, password=pas, host=host, port=port)
    val = []
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con:
        cur = con.cursor()
        cur.execute(str(query))
        rows = cur.fetchall()
        p = [n.name for n in cur.description].index("geom")
        ro = [n.name for n in cur.description]
        del ro[p]
        val.append(ro)
        for row in rows:
            ri = list(row)
            del ri[p]
            nrow = ri
            val.append(nrow)
    print "Excel export OK!"
    return val

def make_excel(table,export_path,pgtable_name):
    #save_file = easygui.filesavebox("Excel Estaciones", "Open File", '.xlsx',
    #                               filetypes=["*.xls", ["*.xlsx", "Excel 2010 files"]])
    save_file = "{export_path}\{pgtable_name}.xlsx".format(pgtable_name=pgtable_name, export_path=export_path)
    workbook = xlsxwriter.Workbook(r''+save_file)
    worksheet = workbook.add_worksheet()
    for row,data in enumerate(table):
        worksheet.write_row(row,0,data)
    workbook.close()
