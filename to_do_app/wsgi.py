import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from . import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_app.settings')

application = get_wsgi_application()
application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
