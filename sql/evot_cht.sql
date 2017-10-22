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

---Ctt (tmed mes)Tco---
CREATE FUNCTION evot_cht_ctt(double precision) RETURNS double precision 
    AS 'select 0.43+0.425*($1/20)+0.122*($1/20)^2;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;

---Cwt (velocidad media del viento mes a 2m de altura, en km/hora)Wo---
CREATE FUNCTION evot_cht_cwt(double precision) RETURNS double precision 
    AS 'select 0.672+0.406*($1/6.7)-0.078*($1/6.7)^2;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;


---Cht (porcentaje de brillo solar medio, en decimales)So---
CREATE FUNCTION evot_cht_cst(double precision) RETURNS double precision 
    AS 'select 0.34+0.856*($1/0.8)-0.196*($1/0.8)^2;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;


---Ce (porcentaje de brillo solar medio, en decimales)Eo---
CREATE FUNCTION evot_cht_ce(double precision) RETURNS double precision 
    AS 'select 0.97+0.03*($1/305);'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;

select evot_cht_cst(0.59)

0.34+0.856*(N41/O41)-0.196*(N41/O41)^2

select evot_cht_cht(0.69)


select evot_cht_cwt(4.5)

=0.672+0.406*($1/6.7)-0,078*($1/6.7)^2
select evot_cht_ctt(28.4)


=0.43+0.425*($1/20)+0.122*($1/20)^2


select 14.398 * dias.total from dias where dias.mes='diciembre' 

select evot_cht_rtt(14.398 ,'diciembre')