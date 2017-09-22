
@echo off
echo
echo "hello world 1!"

goto that

:back
echo "hello world 4!"
goto there

:that
echo "hello world 2!"
goto back

:there
echo "hello world 4!"

@REM start explorer F:\LM
@REM start explorer http:\\g.space-time.site
