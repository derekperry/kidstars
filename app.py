from __future__ import absolute_import
from __future__ import print_function

import os

from flask import Flask, redirect, url_for, Blueprint
from flask_util_js import FlaskUtilJs
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_social import Social
from flask_social.datastore import SQLAlchemyConnectionDatastore

from vivi.models import db, User, Role, Connection

app = Flask(__name__)
try:
    app.config.from_object('vivi.instance.config.{}Config'.format(os.environ['PYENVT']))
except KeyError:
    app.config.from_object('config.Config') # TODO: Change this back to config.Config

db.init_app(app)
fujs = FlaskUtilJs(app)
mail = Mail(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
Security(app, user_datastore)
Social(app, SQLAlchemyConnectionDatastore(db, Connection))

from vivi.views import root
app.register_blueprint(root)


"""
@app.before_first_request
def create_user():
    user_datastore.create_user(email='derek@derekperry.com', password='password')
    db.session.commit()
"""

if __name__ == '__main__':
    app.run()
