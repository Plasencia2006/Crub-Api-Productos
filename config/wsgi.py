import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Esto le ayuda a Vercel a encontrar la variable 'app' que busca por defecto
app = application