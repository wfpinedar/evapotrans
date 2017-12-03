import os
from osgeo import gdal


def make_rast(mtd, ruta):
    ruta_shp = ruta + r"\%s.shp" % (mtd)
    ruta_raster = ruta+"\%s" % (mtd)
    meses = ["evt_enero", "evt_febrer", "evt_marzo", "evt_abril", "evt_mayo", "evt_junio", "evt_julio",
             "evt_agosto", "evt_septie", "evt_octubr", "evt_noviem", "evt_diciem", "anual"]
    try:
        os.stat(ruta_raster)
    except:
        os.mkdir(ruta_raster)
    for i in meses:
        gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
              layers="%s"%(mtd),
              zfield='%s'%(i),
              algorithm='invdist:power=4.0:max_points=25:min_points=1:radius=0.0001',
              format='GTiff',
              width=500, height=500)
    print "Raster export OK!!!"