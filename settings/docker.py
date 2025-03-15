import os
from .base import *


SECRET_KEY = open(Path(os.getenv('WEBAPP_CONF_DIR')) / 'secret-key').read().strip()

DEBUG = False
# DEBUG = True

# ALLOWED_HOSTS = ['.g3.net.pl']
ALLOWED_HOSTS = ['185.242.135.71']

DATA_DIR = Path(os.getenv('WEBAPP_SRV_DIR'))

STATIC_ROOT = DATA_DIR / 'static'

MEDIA_ROOT = DATA_DIR / 'media'

MEDIA_URL = '/media/'