@echo off
title EXTREME3D Manager
cd /d "%~dp0"

echo.
echo  ==========================================
echo        EXTREME 3D - Iniciando...
echo  ==========================================
echo.

:: Tenta Python 3
python --version >nul 2>&1
if %errorlevel% equ 0 (
    python iniciar.py
    goto fim
)

:: Tenta py launcher
py --version >nul 2>&1
if %errorlevel% equ 0 (
    py iniciar.py
    goto fim
)

:: Python nao encontrado
echo  [ERRO] Python nao encontrado!
echo.
echo  1. Acesse: https://www.python.org/downloads/
echo  2. Clique em "Download Python"
echo  3. Na instalacao, marque: "Add Python to PATH"
echo  4. Instale e tente novamente
echo.
pause
exit /b

:fim
pause
