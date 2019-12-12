import sqlite3
import os

import click

from alayatodo import app
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
        db = connect_db()

        if 'db' not in g:
            g.db = db
            
            return g.db
        
        return db

def connect_db():
    db = sqlite3.connect(
        os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + app.config['DATABASE'])
    )
    db.row_factory = sqlite3.Row

    return db

def close_db(e=None):
    db = g.pop('db', None)

    if(db is not None):
        db.close()
