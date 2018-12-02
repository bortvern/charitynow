"""
WSGI config for cngproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
import site
site.addsitedir('/opt/cngproject/cngprojectenv/lib/python3.6/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cngproject.settings')

application = get_wsgi_application()

path = '/opt/cngproject/cngproject'

if path not in sys.path:
    sys.path.append(path)
