@echo off
start cmd /k "cd api && .\venv\Scripts\activate && fastapi run .\app\main.py"
timeout /t 5
start cmd /k "cd app && npm run dev" 