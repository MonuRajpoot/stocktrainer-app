#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # exit on error

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Initialize database (tables will be created automatically by the app)
echo "Database will be initialized on first run..."

echo "Build completed successfully!"
