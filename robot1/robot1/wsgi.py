"""
WSGI config for robot1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"]="robot1.settings"
apache_configuration = os.path.dirname(__file__) 
project = os.path.dirname(apache_configuration) 
sys.path.append(project) 
application = get_wsgi_application()
