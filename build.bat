@echo off
echo ======================================
echo Ses Kayit Edici - Build Script
echo ======================================
echo.

echo Installing dependencies...
pip install -r requirements.txt
pip install cx_Freeze
echo.

echo Building executable...
python setup.py build
echo.

echo Building MSI installer...
python setup.py bdist_msi
echo.

echo ======================================
echo Build completed!
echo ======================================
echo.
echo Executable location: build\
echo MSI installer location: dist\
echo.
pause
