#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "Current directory: $SCRIPT_DIR"

# Use the virtual environment's Python
PYTHON_PATH="$SCRIPT_DIR/venv/bin/python"
echo "Using Python: $PYTHON_PATH"

# Set Django settings module
export DJANGO_SETTINGS_MODULE=core.settings
echo "Django settings module: $DJANGO_SETTINGS_MODULE"

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p staticfiles
mkdir -p media
mkdir -p static

# Add a test static file to ensure there's something to collect
echo "Creating test static file..."
echo "/* Test CSS */" > static/test.css

# Run collectstatic
echo "Running collectstatic..."
$PYTHON_PATH manage.py collectstatic --noinput -v 2

# Check exit status
if [ $? -eq 0 ]; then
    echo "Static files collected successfully"
    echo "Contents of staticfiles directory:"
    ls -la staticfiles/
    
    # Verify the test file was collected
    if [ -f "staticfiles/test.css" ]; then
        echo "Test file successfully collected"
    else
        echo "Warning: Test file not found in staticfiles"
    fi
else
    echo "Error collecting static files"
    echo "Debug information:"
    echo "Django version:"
    $PYTHON_PATH -m django --version
    echo "Settings module: $DJANGO_SETTINGS_MODULE"
    echo "Static root: $(python -c 'from django.conf import settings; print(settings.STATIC_ROOT)')"
    echo "Static dirs: $(python -c 'from django.conf import settings; print(settings.STATICFILES_DIRS)')"
    exit 1
fi

# Create summary of collected files
echo "Static files summary:"
find staticfiles -type f | while read file; do
    echo "  - $file"
done

echo "Build completed successfully"