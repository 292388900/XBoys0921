@echo off 	
echo %~dp0>目录.md

tree /f /a  %1 > 目录.temp
	
for /f "delims=U" %%a in ('cmd/u/cecho 唉') do set "tab=%%a"
echo #目录>>目录.md
echo ### **``时间``** ,*``%date%``*,  `` %time%``>>目录.md
echo.>> 目录.md
set j=0
for /f "delims=""" %%i in (目录.temp) do (
set /a j=j+1
echo %tab%%%i 
echo %tab%%%i >>目录.md
)
echo %j% line
echo %j% line >>目录.md

del 目录.temp
	
pause