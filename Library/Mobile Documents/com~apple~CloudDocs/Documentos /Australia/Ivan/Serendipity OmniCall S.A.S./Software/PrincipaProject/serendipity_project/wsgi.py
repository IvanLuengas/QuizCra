import os

from django.core.wsgi import get_wsgi_application

# Configura la variable de entorno para que Django sepa dónde están los settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serendipity_project.settings')

# Crea la aplicación WSGI.
application = get_wsgi_application()
