-- se tienen en cuentas las siguientes constantes --
-- Tco = 20--
-- Wo = 6.7--
-- Hmo = 0.60--
-- So = 0.80 --
-- Eo = 305 --

---Rtt (radiacion terrestre, mes )---
CREATE FUNCTION evot_cht_rtt(double precision , character varying) RETURNS double precision 
    AS 'select $1 * dias.total from dias where dias.mes=$2 ;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;

---Ctt (tmed mes)---
CREATE FUNCTION evot_cht_ctt(double precision) RETURNS double precision 
    AS 'select $1 * dias.total from dias where dias.mes=$2 ;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;






=0.43+0.425*($2/20)+0.122*($2/20)^2


select 14.398 * dias.total from dias where dias.mes='diciembre' 

select evot_cht_rtt(14.398 ,'diciembre')