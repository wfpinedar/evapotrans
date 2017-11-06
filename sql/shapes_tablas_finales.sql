-- Shape gl

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_gl
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape ln

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_ln
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape turc

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_turc
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape bc

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_bc
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape cht

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_cht
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape har

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_har
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape pm

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(enero) max_enero,max(febrero) max_febrero,max(marzo) max_marzo,max(abril) max_abril,max(mayo) max_mayo,max(junio) max_junio,max(julio) max_julio,max(agosto) max_agosto,max(septiembre) max_septiembre,max(octubre) max_octubre,max(noviembre) max_noviembre,max(diciembre) max_diciembre,
GREATEST(max(enero),max(febrero),max(marzo),max(abril),max(mayo),max(junio),max(julio),max(agosto),max(septiembre),max(octubre),max(noviembre),max(diciembre)) max_anual,
min(enero) min_enero,min(febrero) min_febrero,min(marzo) min_marzo,min(abril) min_abril,min(mayo) min_mayo,min(junio) min_junio,min(julio) min_julio,min(agosto) min_agosto,min(septiembre) min_septiembre,min(octubre) min_octubre,min(noviembre) min_noviembre,min(diciembre) min_diciembre,
LEAST(min(enero),min(febrero),min(marzo),min(abril),min(mayo),min(junio),min(julio),min(agosto),min(septiembre),min(octubre),min(noviembre),min(diciembre)) min_anual,
avg(enero) avg_enero,avg(febrero) avg_febrero,avg(marzo) avg_marzo,avg(abril) avg_abril,avg(mayo) avg_mayo,avg(junio) avg_junio,avg(julio) avg_julio,avg(agosto) avg_agosto,avg(septiembre) avg_septiembre,avg(octubre) avg_octubre,avg(noviembre) avg_noviembre,avg(diciembre) avg_diciembre,
case when avg(enero) IS NULL then 0 else avg(enero) end +
case when avg(febrero) IS NULL then 0 else avg(febrero) end +
case when avg(marzo) IS NULL then 0 else avg(marzo) end +
case when avg(abril) IS NULL then 0 else avg(abril)  end +
case when avg(mayo)  IS NULL then 0 else avg(mayo) end +
case when avg(junio) IS NULL then 0 else avg(junio) end +
case when avg(julio) IS NULL then 0 else avg(julio) end +
case when avg(agosto) IS NULL then 0 else avg(agosto) end  +
case when avg(septiembre) IS NULL then 0 else avg(septiembre) end +
case when avg(octubre) IS NULL then 0 else avg(octubre) end +
case when avg(noviembre) IS NULL then 0 else avg(noviembre) end +
case when avg(diciembre) IS NULL then 0 else avg(diciembre) end as anual
from tmp_evot_pm
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom

-- Shape tw

Select codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom,
max(evt_enero) max_enero,max(evt_febrero) max_febrero,max(evt_marzo) max_marzo,max(evt_abril) max_abril,max(evt_mayo) max_mayo,max(evt_junio) max_junio,max(evt_julio) max_julio,max(evt_agosto) max_agosto,max(evt_septiembre) max_septiembre,max(evt_octubre) max_octubre,max(evt_noviembre) max_noviembre,max(evt_diciembre) max_diciembre,
GREATEST(max(evt_enero),max(evt_febrero),max(evt_marzo),max(evt_abril),max(evt_mayo),max(evt_junio),max(evt_julio),max(evt_agosto),max(evt_septiembre),max(evt_octubre),max(evt_noviembre),max(evt_diciembre)) max_anual,
min(evt_enero) min_enero,min(evt_febrero) min_febrero,min(evt_marzo) min_marzo,min(evt_abril) min_abril,min(evt_mayo) min_mayo,min(evt_junio) min_junio,min(evt_julio) min_julio,min(evt_agosto) min_agosto,min(evt_septiembre) min_septiembre,min(evt_octubre) min_octubre,min(evt_noviembre) min_noviembre,min(evt_diciembre) min_diciembre,
LEAST(min(evt_enero),min(evt_febrero),min(evt_marzo),min(evt_abril),min(evt_mayo),min(evt_junio),min(evt_julio),min(evt_agosto),min(evt_septiembre),min(evt_octubre),min(evt_noviembre),min(evt_diciembre)) min_anual,
avg(evt_enero) avg_enero,avg(evt_febrero) avg_febrero,avg(evt_marzo) avg_marzo,avg(evt_abril) avg_abril,avg(evt_mayo) avg_mayo,avg(evt_junio) avg_junio,avg(evt_julio) avg_julio,avg(evt_agosto) avg_agosto,avg(evt_septiembre) avg_septiembre,avg(evt_octubre) avg_octubre,avg(evt_noviembre) avg_noviembre,avg(evt_diciembre) avg_diciembre,
case when avg(evt_enero) IS NULL then 0 else avg(evt_enero) end +
case when avg(evt_febrero) IS NULL then 0 else avg(evt_febrero) end +
case when avg(evt_marzo) IS NULL then 0 else avg(evt_marzo) end +
case when avg(evt_abril) IS NULL then 0 else avg(evt_abril)  end +
case when avg(evt_mayo)  IS NULL then 0 else avg(evt_mayo) end +
case when avg(evt_junio) IS NULL then 0 else avg(evt_junio) end +
case when avg(evt_julio) IS NULL then 0 else avg(evt_julio) end +
case when avg(evt_agosto) IS NULL then 0 else avg(evt_agosto) end  +
case when avg(evt_septiembre) IS NULL then 0 else avg(evt_septiembre) end +
case when avg(evt_octubre) IS NULL then 0 else avg(evt_octubre) end +
case when avg(evt_noviembre) IS NULL then 0 else avg(evt_noviembre) end +
case when avg(evt_diciembre) IS NULL then 0 else avg(evt_diciembre) end as anual
from tmp_evot_tw
group by codigo,tipo,clase,cat,nombre,municipio,corriente,departamento,altitud,cod_dep,cod_muni,longitud,latitud,estado,geom
