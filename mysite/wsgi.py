"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'mysite.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'mysite.settings'
#getting path 
#path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
#os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
application = get_wsgi_application()
