from voomsdb.settings.base import *
import dj_database_url
from voomsdb.utils.settings import get_env_variable


ALLOWED_HOSTS = ['127.0.0.1']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)rceb+k668zri#f6+r_iesr2@a32zkxuh-2)&3#kfyu(a@gz4="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES["default"] =  dj_database_url.parse(
    get_env_variable("DATABASE_URL"), conn_max_age=600
)

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATIC_DIR = BASE_DIR / 'voomsdb/assets'

STATIC_ROOT = BASE_DIR / "assets"

STATICFILES_DIRS = [
    STATIC_DIR,
]

# Media
MEDIA_URL = "uploads/"

MEDIA_ROOT = BASE_DIR / "uploads"