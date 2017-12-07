@echo off
rem
rem Launch EVOT MASTER
rem
IF EXIST C:\Python27\ArcGIS10.3 SET PATH=%PATH%;C:\Python27\ArcGIS10.3;C:\Python27\ArcGIS10.3\Scripts;C:\Python27\ArcGIS10.3\Lib\site-packages
C:\Python27\ArcGIS10.3\pythonw.exe evot_master.pyw %*
rem
rem Pause on error
rem
if %ERRORLEVEL% GEQ 1 pause
pause