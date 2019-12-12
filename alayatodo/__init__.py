from flask import Flask, g
import sqlite3
from alayatodo.db import db

# configuration
DATABASE = '/tmp/alayatodo.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    db.connect_db()


@app.teardown_request
def teardown_request(exception):
    db.close_db(exception)


import alayatodo.views