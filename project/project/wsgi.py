import os
import sys
from django.core.wsgi import get_wsgi_application

print("WSGI file executed")
print("sys.path:", sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()