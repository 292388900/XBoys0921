@echo off 	
echo %~dp0>Ŀ¼.md

tree /f /a  %1 > Ŀ¼.temp
	
for /f "delims=U" %%a in ('cmd/u/cecho ��') do set "tab=%%a"
echo #Ŀ¼>>Ŀ¼.md
echo ### **``ʱ��``** ,*``%date%``*,  `` %time%``>>Ŀ¼.md
echo.>> Ŀ¼.md
set j=0
for /f "delims=""" %%i in (Ŀ¼.temp) do (
set /a j=j+1
echo %tab%%%i 
echo %tab%%%i >>Ŀ¼.md
)
echo %j% line
echo %j% line >>Ŀ¼.md

del Ŀ¼.temp
	
pause