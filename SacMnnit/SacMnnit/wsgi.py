"""
WSGI config for SacMnnit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#added for heroku
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SacMnnit.settings")

application = get_wsgi_application()

#added for heroku
application = DjangoWhiteNoise(application)









