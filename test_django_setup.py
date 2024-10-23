import os
import django
import sys
from django.conf import settings

def test_django_setup():
    print("=== Django Configuration Test ===")
    print(f"Django Version: {django.get_version()}")
    print(f"Python Path: {sys.path}")
    print(f"Current Directory: {os.getcwd()}")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        django.setup()
        print("Django successfully configured")
        print(f"Static Root: {settings.STATIC_ROOT}")
        print(f"Static URL: {settings.STATIC_URL}")
        return True
    except Exception as e:
        print(f"Error configuring Django: {e}")
        return False

if __name__ == "__main__":
    test_django_setup()