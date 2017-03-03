"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

proxies = {
    "http": os.environ['http://quotaguard8995:948b402a5f97@us-east-1-static.quotaguard.com:9293']
}

res = requests.get("http://ip.jsontest.com/", proxies=proxies)
print res.text