"""
WSGI config for itbook_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itbook_service.settings")
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['192.168.56.101','localhost','127.0.0.1']).split(',')

application = get_wsgi_application()
