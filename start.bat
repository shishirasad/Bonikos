@echo off
title Shishir Varieties POS

:: Always run from the project root (where this file lives)
cd /d "%~dp0"

echo =============================================
echo      SHISHIR VARIETIES POS - STARTUP
echo =============================================
echo.

:: ---------- Python / venv ----------
if exist "venv\Scripts\python.exe" (
    set PYTHON=venv\Scripts\python.exe
    echo [OK] venv found.
) else (
    set PYTHON=python
    echo [WARN] venv not found, using system python.
)

:: ---------- node_modules ----------
if not exist "frontend\node_modules" (
    echo [ERROR] frontend\node_modules not found!
    echo Please open a terminal in E:\atc\frontend and run:  npm install
    pause
    exit /b 1
)

:: ---------- Start Backend ----------
echo.
echo  Starting Backend on the first free port between http://localhost:8000 and http://localhost:8010 ...
start "POS Backend" cmd /k "%PYTHON% -m backend"

:: Give the backend 4 seconds to boot
echo  Waiting 4 seconds for backend...
timeout /t 4 /nobreak > nul

:: ---------- Start Frontend ----------
echo  Starting Frontend on Vite dev server (5173 or next free port) ...
start "POS Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo =============================================
echo  Both windows have been launched.
echo  Backend  : auto-detects a free port in 8000-8010
echo  Frontend : uses 5173 or the next free port if busy
echo =============================================
echo.
echo  You can close this window now.
pause
