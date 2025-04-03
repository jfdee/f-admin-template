@echo off

if not exist venv (
    echo "init venv..."
    CALL python -m venv venv
)

CALL venv\Scripts\activate
CALL python -m pip install -r requirements.txt
