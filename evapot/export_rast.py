import os
import sys
import subprocess

grass7bin = r'C:\OSGeo4W64\bin\grass70.bat'
startcmd = [grass7bin, '--config', 'path']
try:
    p = subprocess.Popen(startcmd, shell=False,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
except OSError as error:
    sys.exit("ERROR: Cannot find GRASS GIS start script"
             " {cmd}: {error}".format(cmd=startcmd[0], error=error))
if p.returncode != 0:
    sys.exit("ERROR: Issues running GRASS GIS start script"
             " {cmd}: {error}"
             .format(cmd=' '.join(startcmd), error=err))
gisbase = str(out.decode('utf-8'))
gisbase = gisbase.rstrip()
os.environ['GISBASE'] = gisbase

#set up GRASS environment variables
grass_pydir = os.path.join(gisbase, "etc", "python")
sys.path.append(grass_pydir)

import grass.script.setup as gsetup

gisdb = os.path.join(os.path.expanduser("~"), "Documents/grassdata")
location = "demolocation"
mapset = "PERMANENT"

rcfile = gsetup.init(gisbase, gisdb, location, mapset)

import grass.script as gscript

#gscript.run_command('g.version', 'c')
#gscript.mapcalc('test2 = sin(col() + row())', flags='g', overwrite=True)
#print gscript.read_command('r.info', map='test1', flags='g')
#print gscript.parse_command('r.univar', map='test1', flags='g')


def make_rast(mtd, ruta):
    ruta_shp = ruta + r"\%s.shp" % (mtd)
    ruta_raster = ruta+"\%s" % (mtd)
    try:
        os.stat(ruta_raster)
    except:
        os.mkdir(ruta_raster)
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_enero", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_ener_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_febrer", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_febr_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_marzo", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_marz_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_abril", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_abri_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_mayo", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_mayo_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_junio", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_juni_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_julio", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_juli_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_agosto", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_agos_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_septie", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_sept_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_octubr", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_octu_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_noviem", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_novi_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_diciem", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_dici_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "max_anual", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//max_anual_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_enero", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_ener_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_febrer", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_febr_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_marzo", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_marz_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_abril", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_abri_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_mayo", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_mayo_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_junio", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_juni_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_julio", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_juli_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_agosto", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_agos_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_septie", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_sept_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_octubr", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_octu_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_noviem", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_novi_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_diciem", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_dici_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "min_anual", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//min_anual_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_enero", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_ener_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_febrer", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_febr_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_marzo", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_marz_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_abril", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_abri_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_mayo", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_mayo_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_junio", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_juni_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_julio", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_juli_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_agosto", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_agos_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_septie", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_sept_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_octubr", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_octu_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_noviem", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_novi_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_diciem", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_dici_%s.tif" % (ruta_raster, mtd))
    gscript.run_command("v.surf.idw", r"%s" % (ruta_shp), 25, 4, "avg_anual", True,
                      "169069.267714,1683910.62887,26811.0059215,1979818.19343", 500, -1, 0.0001,
                      r"%s//avg_anual_%s.tif" % (ruta_raster, mtd))

os.remove(rcfile)
