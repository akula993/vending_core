from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',  # Укажите IP-адрес и порт вашего Memcached-сервера
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / 'static_src',
                    # 'static/'
                    ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


