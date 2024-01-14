import os
import re


PATTERN = re.compile('^[0-9a-zA-Z]+$')
MAX_LENGTH = 16
MAX_CHARACTER = 6


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_YA', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')
