import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'street_safe.settings'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
