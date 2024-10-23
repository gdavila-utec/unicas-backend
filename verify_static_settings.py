import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

def verify_static_settings():
    print("=== Static Files Configuration ===")
    
    # Check INSTALLED_APPS
    if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
        print("✓ staticfiles app is installed")
    else:
        print("✗ staticfiles app is missing")
        return False
    
    # Check static files settings
    print(f"\nStatic Files Settings:")
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATICFILES_DIRS: {getattr(settings, 'STATICFILES_DIRS', [])}")
    
    # Check directories
    if os.path.exists(settings.STATIC_ROOT):
        print(f"✓ STATIC_ROOT directory exists: {settings.STATIC_ROOT}")
    else:
        print(f"✗ STATIC_ROOT directory missing: {settings.STATIC_ROOT}")
    
    for static_dir in getattr(settings, 'STATICFILES_DIRS', []):
        if os.path.exists(static_dir):
            print(f"✓ Static directory exists: {static_dir}")
        else:
            print(f"✗ Static directory missing: {static_dir}")
    
    return True

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    import django
    django.setup()
    
    if verify_static_settings():
        print("\nTrying to collect static files...")
        try:
            execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '-v2'])
            print("✓ collectstatic successful")
        except Exception as e:
            print(f"✗ collectstatic failed: {e}")
    else:
        print("\n✗ Static files configuration is incomplete")