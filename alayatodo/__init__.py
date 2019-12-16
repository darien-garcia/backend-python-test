from flask import Flask
from alayatodo.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import auth
app.register_blueprint(auth.bp)

from . import todos
app.register_blueprint(todos.bp)

from alayatodo import models