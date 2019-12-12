import sqlite3
import os

import click

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
        db = connect_db()

        if 'db' not in g:
            g.db = db
            
            return g.db
        
        return db

def connect_db():
    return create_db_connection(current_app.config['DATABASE'])

def create_db_connection(database):
    db = sqlite3.connect(
        os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + database)
    )
    db.row_factory = sqlite3.Row

    return db

def close_db(e=None):
    db = g.pop('db', None)

    if(db is not None):
        db.close()
