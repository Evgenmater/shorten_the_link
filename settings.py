import os

LOCAL_HOST = os.getenv('LOCAL_HOST', default='http://localhost/')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_YA', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')
