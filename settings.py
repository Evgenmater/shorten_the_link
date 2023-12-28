import os

LOCAL_HOST = os.getenv('LOCAL_HOST', default='HOST')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_YA', default='DATABASE_YA')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='KEY')
