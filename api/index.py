from api import routes
from flask import Flask
from api.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

index = Flask(__name__)
index.config.from_object(Config)
db = SQLAlchemy(index)
migrate = Migrate(index, db)
