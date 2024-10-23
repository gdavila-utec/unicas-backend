import os
import sys
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

def handler(request, **kwargs):
    if request.get('method') == 'OPTIONS':
        return {
            'statusCode': 204,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type, Accept, Authorization, x-clerk-auth-status, x-clerk-auth-token',
                'Access-Control-Max-Age': '86400',
                'Content-Type': 'text/plain',
                'Content-Length': '0'
            },
            'body': ''
        }
    
    try:
        return application(request, **kwargs)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'type': str(type(e).__name__)
            })
        }