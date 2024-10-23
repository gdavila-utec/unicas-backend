import os
import sys
from core.wsgi import application

def handler(request, **kwargs):
    try:
        return application(request, **kwargs)
    except Exception as e:
        error_message = f"Error processing request: {str(e)}"
        print(error_message, file=sys.stderr)
        
        # Return a more detailed error response
        response_body = {
            "error": "Internal Server Error",
            "detail": str(e) if os.getenv('DEBUG') == 'True' else "An error occurred",
            "type": "FUNCTION_INVOCATION_FAILED"
        }
        
        return {
            "statusCode": 500,
            "body": response_body,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "X-Requested-With, Content-Type, Accept, Authorization"
            }
        }