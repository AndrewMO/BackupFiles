@echo off
set mode=%1
echo "mode=%mode%"

if "%mode%"=="local" (
    goto local
)else (
    goto remote
	)



:local
python "C:\ajia\RushPoolPYProject\RushPool_StopService.py"
goto end
:remote
python "C:\ajia\RushPoolPYProject\RushPool_StopCache.py"
python "C:\ajia\RushPoolPYProject\RushPool_StopService.py"
goto end
:end
exit
