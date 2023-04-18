from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['akula-inc.online', 'www.akula-inc.online',]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'akula993@gmail.com'
EMAIL_HOST_PASSWORD = 'postojrkzxzihejp'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': 'unix:///home/users/a/akula993/memcached/memcached.sock',  # Укажите IP-адрес и порт вашего Memcached-сервера
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'akula993_vending',
        'USER': 'akula993',
        'PASSWORD': 'wind2606',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}



STATIC_URL = 'public_html/static/'
STATIC_ROOT = BASE_DIR / 'public_html/static'
STATICFILES_DIRS = [BASE_DIR / 'static',
                    # 'static/'
                    ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
