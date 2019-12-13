from flask import Flask, g
import sqlite3
import os

from flask import Flask


def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG = True,
        DATABASE='/tmp/alayatodo.db',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import auth
    app.register_blueprint(auth.bp)

    from . import todos
    app.register_blueprint(todos.bp)

    return app

