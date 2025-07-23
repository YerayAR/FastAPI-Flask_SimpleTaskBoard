@echo off
cd /d "C:\Users\yera2\Dev\fastAPI-Flask-SimpleTaskBoard"
call venv\Scripts\activate.bat
set FASTAPI_URL=http://localhost:8000
echo Starting Flask server on http://localhost:5000
python -m frontend.app
pause
