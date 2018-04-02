import os
from datetime import timedelta

# For app
DEBUG = True

# Keys
SECRET_KEY = 'development_qara'

# For MySQL Database

DB_HOST = os.environ.get('localhost')
DB_NAME = 'qaradb'
DB_PORT = 3306
DB_USER = 'qara'
DB_PASSWORD = 'qara2580'

#DB_HOST = os.environ.get('DB_HOST')
#DB_NAME = os.environ.get('DB_NAME')
#DB_PORT = os.environ.get('DB_PORT')
#DB_USER = os.environ.get('DB_USER')
#DB_PASSWORD = os.environ.get('DB_PASSWORD')

# For session
SESSION_COOKIE_NAME = 'qara_sc'
PERMANENT_SESSION_LIFETIME = timedelta(31)
