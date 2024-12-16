#!/bin/bash
echo "Setting up Battery Aging Analysis Project"

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Run initial analysis
python main.py

echo "Setup Complete!"