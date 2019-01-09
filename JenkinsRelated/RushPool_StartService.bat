@echo off
set mode=%1
echo "mode=%mode%"

if "%mode%"=="local" (
    goto local
)else (
    goto remote
	)



:local
echo "srarting..."
python "C:\ajia\RushPoolPYProject\RushPool_StartService.py"
goto end
:remote
echo "srarting cache..."
python "C:\ajia\RushPoolPYProject\RushPool_StartCache.py"
echo "srarting servlet..."
python "C:\ajia\RushPoolPYProject\RushPool_StartService.py"
goto end
:end
exit
