import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'village_management.settings')

# Django WSGI application
application = get_wsgi_application()

# Vercel expects a variable named `app`
app = application
