@echo off
echo 当前目录
echo %cd%

echo.
echo 计算机名称
echo %COMPUTERNAME%

echo.
echo 返回当前时间
echo %date% , %time%

echo.
echo 随机数
echo %random%

echo.
echo 系统 指定安装在计算机上的处理器的数目
echo %NUMBER_OF_PROCESSORS% 

echo.
echo 操作系统名称
echo %OS%

echo.
echo 系统 返回处理器的芯片体系结构。值：x86 或 IA64 基于Itanium
echo %PROCESSOR_ARCHITECTURE% 

echo.
echo 系统 返回处理器说明。
echo  %PROCESSOR_IDENTFIER%

echo.
echo 系统 返回计算机上安装的处理器的型号。 
echo %PROCESSOR_LEVEL%

echo.
echo  系统 返回处理器的版本号。
echo %PROCESSOR_REVISION%

echo.
echo %0

pause