# app/__init__.py

from flask import Flask
from config import Config


#initalize the app

app = Flask(__name__, instance_relative_config=True)


# Load the views
from app import views


# Load the config file
#error when capitalizing C

app.config.from_object('config')