@echo off

set "is_environment_activated=false"

if exist "venv\" (
	echo Virtual environment detected.
	goto RunGame
) else (
	goto CreateEnvironment
)

:CreateEnvironment
echo Creating environment...
python -m venv venv
call venv\Scripts\activate.bat
set "is_environment_activated=true"
pip install windows-curses


:RunGame
if "%is_environment_activated%"=="false" (
	echo Running game...
	call venv\Scripts\activate.bat
	set "is_environment_activated=true"
)

python main.py

exit
