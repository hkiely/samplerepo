# Enable Flask's debugging features. Should be False in production
import os

DEBUG = True

#utilize class to store configuration variables.
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess'