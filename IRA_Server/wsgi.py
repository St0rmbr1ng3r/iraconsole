"""
WSGI config for IRA_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
'''
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IRA_Server.settings')

application = get_wsgi_application()

'''

import os
import sys
sys.path.append('/opt/bitnami/Apps/iraconsole/IRA_Server')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/Apps/iraconsole/IRA_Server/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "/opt/bitnami/Apps/iraconsole/IRA_Server/IRA_Server.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
