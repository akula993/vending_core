from settings import *

DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = 'address_list'

# AUTH_USER_MODEL = 'vendings.CustomUser'
LOGIN_URL = '/accounts/login/'  # URL для страницы входа
LOGOUT_URL = '/accounts/logout/'  # URL для страницы выхода

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'akula993@gmail.com'
# EMAIL_HOST_PASSWORD = 'postojrkzxzihejp'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / 'static_src',
                    # 'static/'
                    ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
