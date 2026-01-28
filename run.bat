@echo off
echo.
echo ========================================
echo  LensaSiaga - AI Disaster Detection
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
python --version

echo.
echo [2/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [3/4] Checking model files...
if not exist "mobilenet_final_model.h5" (
    echo WARNING: mobilenet_final_model.h5 not found
    echo Please ensure the model file is in the current directory
)
if not exist "class_names.json" (
    echo WARNING: class_names.json not found
    echo Please ensure the class names file is in the current directory
)

echo.
echo [4/4] Starting LensaSiaga...
echo.
echo ========================================
echo  Application will open in your browser
echo  URL: http://localhost:8501
echo ========================================
echo.
streamlit run app.py

pause
