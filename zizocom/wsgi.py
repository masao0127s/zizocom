"""
WSGI config for zizocom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
# ----- 他のアプリと同居させるための設定 -----
sys.path.append('/var/www/zizocom')
sys.path.append('/var/www/zizocom/zizocom')
# ----- 他のアプリと同居させるための設定 -----

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zizocom.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
