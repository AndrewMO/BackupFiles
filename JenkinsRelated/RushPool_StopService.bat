@echo off
set mode=%1
echo "mode=%mode%"

if "%mode%"=="local" (
    goto local
)else (
    goto remote
	)



:local
python "C:\ajia\RushPoolPYProject\RushPool_Initialing.py"
goto end
:remote
python "C:\ajia\RushPoolPYProject\RushPool_Initialing.py"
python "C:\ajia\RushPoolPYProject\RushPool_Initialing.py"
goto end
:end
exit
