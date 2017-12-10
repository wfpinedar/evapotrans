
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


def tmp_prom_dec(usr,pas,port,host,bd):
    exec('''con1 = psycopg2.connect(database=bd, user=usr, password=pas, host=host, port=port)''')
    exec ('''con1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)''')
    exec('''cursor1 = con1.cursor()''')
    exec ('''cursor1.execute(  %s CREATE table tmp_dec_pm as (
    SELECT
     estacion.*,
     tmin.decada AS Decada,
     tmin.anio,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='enero') * evot_pm_eto(latitud, altitud,tmax.enero,tmin.enero,tmedia.enero,humedad.enero,brillo.enero,velocidad.enero,'enero')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='enero') * evot_pm_eto(latitud, altitud,tmax.enero,tmin.enero,tmedia.enero,humedad.enero,brillo.enero,velocidad.enero,'enero')
    else
    (select d3 from dias where mes ='enero') * evot_pm_eto(latitud, altitud,tmax.enero,tmin.enero,tmedia.enero,humedad.enero,brillo.enero,velocidad.enero,'enero')
    end AS evot_enero,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='febrero') * evot_pm_eto(latitud, altitud,tmax.febrero,tmin.febrero,tmedia.febrero,humedad.febrero,brillo.febrero,velocidad.febrero,'febrero')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='febrero') * evot_pm_eto(latitud, altitud,tmax.febrero,tmin.febrero,tmedia.febrero,humedad.febrero,brillo.febrero,velocidad.febrero,'febrero')
    else
    (select d3 from dias where mes ='febrero') * evot_pm_eto(latitud, altitud,tmax.febrero,tmin.febrero,tmedia.febrero,humedad.febrero,brillo.febrero,velocidad.febrero,'febrero')
    end AS evot_febrero,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='marzo') * evot_pm_eto(latitud, altitud,tmax.marzo,tmin.marzo,tmedia.marzo,humedad.marzo,brillo.marzo,velocidad.marzo,'marzo')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='marzo') * evot_pm_eto(latitud, altitud,tmax.marzo,tmin.marzo,tmedia.marzo,humedad.marzo,brillo.marzo,velocidad.marzo,'marzo')
    else
    (select d3 from dias where mes ='marzo') * evot_pm_eto(latitud, altitud,tmax.marzo,tmin.marzo,tmedia.marzo,humedad.marzo,brillo.marzo,velocidad.marzo,'marzo')
    end AS evot_marzo,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='abril') * evot_pm_eto(latitud, altitud,tmax.abril,tmin.abril,tmedia.abril,humedad.abril,brillo.abril,velocidad.abril,'abril')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='abril') * evot_pm_eto(latitud, altitud,tmax.abril,tmin.abril,tmedia.abril,humedad.abril,brillo.abril,velocidad.abril,'abril')
    else
    (select d3 from dias where mes ='abril') * evot_pm_eto(latitud, altitud,tmax.abril,tmin.abril,tmedia.abril,humedad.abril,brillo.abril,velocidad.abril,'abril')
    end AS evot_abril,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='mayo') * evot_pm_eto(latitud, altitud,tmax.mayo,tmin.mayo,tmedia.mayo,humedad.mayo,brillo.mayo,velocidad.mayo,'mayo')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='mayo') * evot_pm_eto(latitud, altitud,tmax.mayo,tmin.mayo,tmedia.mayo,humedad.mayo,brillo.mayo,velocidad.mayo,'mayo')
    else
    (select d3 from dias where mes ='mayo') * evot_pm_eto(latitud, altitud,tmax.mayo,tmin.mayo,tmedia.mayo,humedad.mayo,brillo.mayo,velocidad.mayo,'mayo')
    end AS evot_mayo,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='junio') * evot_pm_eto(latitud, altitud,tmax.junio,tmin.junio,tmedia.junio,humedad.junio,brillo.junio,velocidad.junio,'junio')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='junio') * evot_pm_eto(latitud, altitud,tmax.junio,tmin.junio,tmedia.junio,humedad.junio,brillo.junio,velocidad.junio,'junio')
    else
    (select d3 from dias where mes ='junio') * evot_pm_eto(latitud, altitud,tmax.junio,tmin.junio,tmedia.junio,humedad.junio,brillo.junio,velocidad.junio,'junio')
    end AS evot_junio,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='julio') * evot_pm_eto(latitud, altitud,tmax.julio,tmin.julio,tmedia.julio,humedad.julio,brillo.julio,velocidad.julio,'julio')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='julio') * evot_pm_eto(latitud, altitud,tmax.julio,tmin.julio,tmedia.julio,humedad.julio,brillo.julio,velocidad.julio,'julio')
    else
    (select d3 from dias where mes ='julio') * evot_pm_eto(latitud, altitud,tmax.julio,tmin.julio,tmedia.julio,humedad.julio,brillo.julio,velocidad.julio,'julio')
    end AS evot_julio,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='agosto') * evot_pm_eto(latitud, altitud,tmax.agosto,tmin.agosto,tmedia.agosto,humedad.agosto,brillo.agosto,velocidad.agosto,'agosto')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='agosto') * evot_pm_eto(latitud, altitud,tmax.agosto,tmin.agosto,tmedia.agosto,humedad.agosto,brillo.agosto,velocidad.agosto,'agosto')
    else
    (select d3 from dias where mes ='agosto') * evot_pm_eto(latitud, altitud,tmax.agosto,tmin.agosto,tmedia.agosto,humedad.agosto,brillo.agosto,velocidad.agosto,'agosto')
    end AS evot_agosto,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='septiembre') * evot_pm_eto(latitud, altitud,tmax.septiembre,tmin.septiembre,tmedia.septiembre,humedad.septiembre,brillo.septiembre,velocidad.septiembre,'septiembre')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='septiembre') * evot_pm_eto(latitud, altitud,tmax.septiembre,tmin.septiembre,tmedia.septiembre,humedad.septiembre,brillo.septiembre,velocidad.septiembre,'septiembre')
    else
    (select d3 from dias where mes ='septiembre') * evot_pm_eto(latitud, altitud,tmax.septiembre,tmin.septiembre,tmedia.septiembre,humedad.septiembre,brillo.septiembre,velocidad.septiembre,'septiembre')
    end AS evot_septiembre,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='octubre') * evot_pm_eto(latitud, altitud,tmax.octubre,tmin.octubre,tmedia.octubre,humedad.octubre,brillo.octubre,velocidad.octubre,'octubre')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='octubre') * evot_pm_eto(latitud, altitud,tmax.octubre,tmin.octubre,tmedia.octubre,humedad.octubre,brillo.octubre,velocidad.octubre,'octubre')
    else
    (select d3 from dias where mes ='octubre') * evot_pm_eto(latitud, altitud,tmax.octubre,tmin.octubre,tmedia.octubre,humedad.octubre,brillo.octubre,velocidad.octubre,'octubre')
    end AS evot_octubre,

     case when tmin.decada = '1' then
     (select d1 from dias where mes ='noviembre') * evot_pm_eto(latitud, altitud,tmax.noviembre,tmin.noviembre,tmedia.noviembre,humedad.noviembre,brillo.noviembre,velocidad.noviembre,'noviembre')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='noviembre') * evot_pm_eto(latitud, altitud,tmax.noviembre,tmin.noviembre,tmedia.noviembre,humedad.noviembre,brillo.noviembre,velocidad.noviembre,'noviembre')
    else
    (select d3 from dias where mes ='noviembre') * evot_pm_eto(latitud, altitud,tmax.noviembre,tmin.noviembre,tmedia.noviembre,humedad.noviembre,brillo.noviembre,velocidad.noviembre,'noviembre')
    end AS evot_noviembre,

      case when tmin.decada = '1' then
     (select d1 from dias where mes ='diciembre') * evot_pm_eto(latitud, altitud,tmax.diciembre,tmin.diciembre,tmedia.diciembre,humedad.diciembre,brillo.diciembre,velocidad.diciembre,'diciembre')
    when tmin.decada = '2' then
    (select d2 from dias where mes ='diciembre') * evot_pm_eto(latitud, altitud,tmax.diciembre,tmin.diciembre,tmedia.diciembre,humedad.diciembre,brillo.diciembre,velocidad.diciembre,'diciembre')
    else
    (select d3 from dias where mes ='diciembre') * evot_pm_eto(latitud, altitud,tmax.diciembre,tmin.diciembre,tmedia.diciembre,humedad.diciembre,brillo.diciembre,velocidad.diciembre,'diciembre')
    end AS evot_diciembre

    FROM
    (SELECT   estacion.* FROM estacion) AS estacion,
    (SELECT codigo,anio,decada,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre FROM prom_dec WHERE variable='TMN') AS tmin,
    (SELECT codigo,anio,decada,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre FROM prom_dec WHERE variable='TMX') AS tmax,
    (SELECT codigo,anio,decada,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre FROM prom_dec WHERE variable='TMD') AS tmedia,
    (SELECT codigo,anio,decada,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre FROM prom_dec WHERE variable='BS') AS brillo,
    (SELECT codigo,anio,decada,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre FROM prom_dec WHERE variable='HR') AS humedad,
    (SELECT codigo,anio,decada,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre FROM prom_dec WHERE variable='VD') AS velocidad
    WHERE
    estacion.codigo =  tmin.codigo AND
    estacion.codigo =  tmax.codigo AND
    estacion.codigo =  tmedia.codigo AND
    estacion.codigo =  brillo.codigo AND
    estacion.codigo =  humedad.codigo AND
    estacion.codigo =  velocidad.codigo AND
    velocidad.anio =  tmin.anio AND
    tmin.anio =  tmax.anio AND
    tmax.anio =  tmedia.anio AND
    tmedia.anio =  brillo.anio AND
    brillo.anio =  humedad.anio AND
    humedad.anio =  velocidad.anio AND
    velocidad.decada =  tmin.decada AND
    tmin.decada =  tmax.decada AND
    tmax.decada =  tmedia.decada AND
    tmedia.decada =  brillo.decada AND
    brillo.decada =  humedad.decada AND
    humedad.decada =  velocidad.decada ) %s )'''%("'''","'''"))