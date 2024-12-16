@echo off
echo Setting up Battery Aging Analysis Project

# Create virtual environment
python -m venv venv

# Activate virtual environment
call venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Run initial analysis
python main.py

echo Setup Complete!
pause