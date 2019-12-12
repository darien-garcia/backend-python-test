from flask import Flask, g
import sqlite3
from alayatodo.db import db
from alayatodo.auth import auth

# configuration
DATABASE = '/tmp/alayatodo.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def create_app():

        app = Flask(__name__)
        app.config.from_object(__name__)

        app.register_blueprint(auth.bp)

        
        return app


import alayatodo.views