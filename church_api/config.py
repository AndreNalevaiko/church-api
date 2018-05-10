import os

APP_NAME = 'optilab-bi-api'
APP_VERSION = '1.0.0'
API_VERSION = 'v1'

DATABASE_URL = os.environ['DATABASE_MYSQL']

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_MAX_OVERFLOW = 10
SQLALCHEMY_POOL_RECYCLE = 60 * 5
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_MYSQL']
SQLALCHEMY_ECHO = False