from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ALLOWED_HOSTS = ['test.akula-inc.online', 'www.test.akula-inc.online', '192.168.1.115', '91.107.42.161',]
ALLOWED_HOSTS = ['*',]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'akula993@gmail.com'
EMAIL_HOST_PASSWORD = 'postojrkzxzihejp'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
        # Укажите IP-адрес и порт вашего Memcached-сервера
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'akula993_vending',
	'NAME': 'uakula993',
        'USER': 'akula993',
        'PASSWORD': 'wind2606',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '/var/work/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',
                    'static_src',
                    ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
