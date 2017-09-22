::这是注释
@REM 这也是注释

@REM 设置标题
title test2

@REM 设置颜色
color F0

@REM 设置大小
mode con cols=100 lines=60 

@REM start explorer F:\LM
@REM start explorer http:\\g.space-time.site

@echo off

echo "hello world0!"

call test.bat

echo "hello world5!"

echo %0
@REM  换行
echo.
@REM ^是转义字符
echo 按任意键继续^^_^^& pause >nul