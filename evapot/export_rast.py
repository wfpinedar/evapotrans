import os
from osgeo import gdal


def make_rast(mtd, ruta, period):
    ruta_shp = ruta + r"\%s.shp" % (mtd)
    ruta_raster = ruta+"\%s" % (mtd)
    meses = ["evt_enero", "evt_febrer", "evt_marzo", "evt_abril", "evt_mayo", "evt_junio", "evt_julio",
             "evt_agosto", "evt_septie", "evt_octubr", "evt_noviem", "evt_diciem", "anual"]
    decadas = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10",
               "d11", "d12", "d13", "d14", "d15", "d16", "d17", "d18", "d19", "d20",
               "d21", "d22", "d23", "d24", "d25", "d26", "d27", "d28", "d29", "d30",
               "d31", "d32", "d33", "d34", "d35", "d36"]
    try:
        os.stat(ruta_raster)
    except:
        os.mkdir(ruta_raster)
    if period == 'Mensual':
        for i in meses:
            gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
                  layers="%s"%(mtd),
                  zfield='%s'%(i),
                  algorithm='invdist:power=4.0:max_points=25:min_points=1:radius=0.0001:nodata=100.0',
                  format='GTiff',
                  width=500, height=500)
    elif period == 'Decadal':
        for i in decadas:
            gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
                  layers="%s"%(mtd),
                  zfield='%s'%(i),
                  algorithm='invdist:power=4.0:max_points=25:min_points=1:radius=0.0001:nodata=60.0',
                  format='GTiff',
                  width=500, height=500)
    print "Raster export OK!!!"