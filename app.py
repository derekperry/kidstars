from __future__ import absolute_import

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_util_js import FlaskUtilJs
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_social import Social
from flask_social.datastore import SQLAlchemyConnectionDatastore

from models import User, Role, Connection

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
fujs = FlaskUtilJs(app)
mail = Mail(app)
Security(app, SQLAlchemyUserDatastore(db, User, Role))
Social(app, SQLAlchemyConnectionDatastore(db, Connection))


@app.route('/')
def hello_world():
    return 'Hello World!'

@login_required
@app.route('/1')
def hello_world1():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
