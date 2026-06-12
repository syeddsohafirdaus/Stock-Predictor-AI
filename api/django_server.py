# api/django_server.py
import os
import sys
from pathlib import Path

# Add project root to PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InternationalStock.settings')
import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def handler(event, context):
    """Vercel Python serverless entry point.
    Forwards request to Django WSGI app and returns response.
    """
    from werkzeug.wrappers import Request, Response
    # Convert Vercel event dict to a WSGI environ
    req = Request(event)
    resp = Response.from_app(application, req.environ)
    return {
        "statusCode": resp.status_code,
        "headers": dict(resp.headers),
        "body": resp.get_data(as_text=True)
    }
