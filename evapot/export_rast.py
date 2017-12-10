import os
from osgeo import gdal

# pow,max,min,rad,nodata,left,bot,right,top,alto,ancho
def make_rast(mtd, ruta, period,tipo,pow,max,min,rad,nodata,left,bot,right,top,alto,ancho):
    decadas = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10",
               "d11", "d12", "d13", "d14", "d15", "d16", "d17", "d18", "d19", "d20",
               "d21", "d22", "d23", "d24", "d25", "d26", "d27", "d28", "d29", "d30",
               "d31", "d32", "d33", "d34", "d35", "d36"]
    if tipo=="Resultado":
        ruta_raster = ruta+"\%s_rasters" % (mtd)
        meses = ["evt_enero", "evt_febrero", "evt_marzo", "evt_abril", "evt_mayo", "evt_junio", "evt_julio",
                 "evt_agosto", "evt_septiembre", "evt_octubre", "evt_noviembre", "evt_diciembre", "anual"]
        try:
            os.stat(ruta_raster)
        except:
            os.mkdir(ruta_raster)
        if period == 'Mensual':
            for i in meses:
                ruta_shp = ruta + r"\%s_shapes\%s_%s.shp" % (mtd, mtd, i)
                gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
                          layers="%s_%s" % (mtd, i),
                          zfield='%s' % (i[:10]),
                          outputBounds=[left, bot, right, top],
                          algorithm='invdist:power=%d:max_points=%d:min_points=%d:radius=%d:nodata=%d'%(pow,max,min,rad,nodata),
                          format='GTiff',
                          width=ancho, height=alto)
        elif period == 'Decadal':
            for i in decadas:
                ruta_shp = ruta + r"\%s_shapes\%s_%s.shp" % (mtd,mtd,i)
                gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
                      layers="%s_%s"%(mtd,i),
                      zfield='%s'%(i),
                      outputBounds=[left, bot, right, top],
                          algorithm='invdist:power=%d:max_points=%d:min_points=%d:radius=%d:nodata=%d' % (
                          pow, max, min, rad, nodata),
                      format='GTiff',
                      width=ancho, height=alto)
        print "Raster export OK!!!"

    else: #variables
        meses_var = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                     "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

        ruta_raster = ruta + "\%s_rasters" % (mtd)
        try:
            os.stat(ruta_raster)
        except:
            os.mkdir(ruta_raster)

        if period == 'Decadal':
            for i in meses_var:
                ruta_shp = ruta + r"\%s_shapes\%s_%s.shp" % (mtd,mtd,i)
                gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
                      layers="%s_%s"%(mtd,i),
                      zfield='%s'%(i),
                      outputBounds=[left, bot, right, top],
                          algorithm='invdist:power=%d:max_points=%d:min_points=%d:radius=%d:nodata=%d' % (
                          pow, max, min, rad, nodata),
                      format='GTiff',
                      width=ancho, height=alto)
            print "Raster export OK!!!"

        if period == 'Mensual':
            for i in meses_var:
                ruta_shp = ruta + r"\%s_shapes\%s_%s.shp" % (mtd, mtd, i)
                gdal.Grid(r"%s//%s_%s.tif" % (ruta_raster, mtd, i), r"%s" % (ruta_shp),
                          layers="%s_%s" % (mtd, i),
                          zfield='%s' % (i[:10]),
                          outputBounds=[left, bot, right, top],
                          algorithm='invdist:power=%d:max_points=%d:min_points=%d:radius=%d:nodata=%d' % (
                          pow, max, min, rad, nodata),
                          format='GTiff',
                          width=ancho, height=alto)