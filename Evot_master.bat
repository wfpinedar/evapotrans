@echo off
rem
rem Launch EVOT MASTER
rem
setlocal
where python > tmp.txt
set /p  pa= < tmp.txt
SET py=%pa:~0,22%

IF EXIST %py% SET PATH=%PATH%;%py%;%py%\Scripts;%py%\Lib\site-packages
%pa% evot_master.pyw > run.log %*
rem
rem Pause on error
rem
if %ERRORLEVEL% GEQ 1 pause
pause