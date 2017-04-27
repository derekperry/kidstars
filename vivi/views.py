from __future__ import absolute_import

from flask import Blueprint
from flask_security import login_required, current_user

root = Blueprint('views', __name__, template_folder='templates')


@root.route('/')
def hello_world():
    if not current_user.is_authenticated:
        return 'Not logged in  - Hello World!'
    else:
        return 'Hello World!'


@root.route('/test')
@login_required
def hello_world1():
    return 'Hello World!'

