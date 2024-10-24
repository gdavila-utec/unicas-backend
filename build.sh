#!/bin/bash
set -e

echo "Creating necessary directories..."
mkdir -p static/admin
mkdir -p static/rest_framework/css
mkdir -p staticfiles
mkdir -p media

echo "Downloading bootstrap..."
curl -o static/rest_framework/css/bootstrap.min.css https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Applying database migrations..."
python manage.py migrate

echo "Build script completed"