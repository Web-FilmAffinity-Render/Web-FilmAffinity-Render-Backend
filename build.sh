#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager 
pip install -r requirements.txt

# Apply any outstanding database migrations
python manage.py migrate