DEBUG = True

ALLOWED_HOSTS = ('*',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'swiftmarket',
        'USER': 'paprika',
        'PASSWORD': 'paprika',
        'HOST': 'localhost',
        'PORT': ''
    }
}