from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cgzefg029oa@84@@*e6*8^tk9ik2i@7(39q$o87)$8pqx0bw8_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    
    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev',
        },
        
    },
    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        }
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')