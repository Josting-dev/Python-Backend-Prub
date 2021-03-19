

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db/mysql/db.mysql'),
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}