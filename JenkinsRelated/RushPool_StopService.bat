@echo off
set mode=%1
echo "mode=%mode%"

if "%mode%"=="local" (
    goto local
)else (
    goto remote
	)



:local
echo "stoping..."
python "C:\ajia\RushPoolPYProject\RushPool_StopService.py"
goto end
:remote
echo "stoping cache..."
python "C:\ajia\RushPoolPYProject\RushPool_StopCache.py"
echo "stoping servlet..."
python "C:\ajia\RushPoolPYProject\RushPool_StopService.py"
goto end
:end
exit
