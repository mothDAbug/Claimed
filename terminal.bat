@echo off
cd /d %~dp0
set VENV_DIR=venv

if not exist "%VENV_DIR%" (
    echo Virtual environment not found. Creating one...
    python -m venv %VENV_DIR%
    echo Virtual environment created successfully.
)

echo Activating virtual environment...
powershell -NoExit -ExecutionPolicy Bypass -Command "& \"%CD%\%VENV_DIR%\Scripts\Activate.ps1\""
