import os
from .base import *


SECRET_KEY = open(Path(os.getenv('WEBAPP_CONF_DIR')) / 'secret-key').read().strip()

DEBUG = False

ALLOWED_HOSTS = ['.g3.net.pl']

DATA_DIR = Path(os.getenv('WEBAPP_SRV_DIR'))

STATIC_ROOT = DATA_DIR / 'static'

MEDIA_ROOT = DATA_DIR / 'media'

MEDIA_URL = '/media/'