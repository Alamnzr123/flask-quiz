# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/alamnzr122/flask-quiz/app.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# from api import index

from api import index
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/alamnzr122/flask-quiz/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['QUES_PER_PAGE'] = 1
db = SQLAlchemy(app)
migrate = Migrate(app, db)
