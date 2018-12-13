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
python "C:\ajia\RushPoolPYProject\RushPool_StartService.py"
goto end
:remote
echo "stoping cache..."
python "C:\ajia\RushPoolPYProject\RushPool_StartCache.py"
echo "stoping servlet..."
python "C:\ajia\RushPoolPYProject\RushPool_StartService.py"
goto end
:end
exit
