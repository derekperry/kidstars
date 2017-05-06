from __future__ import absolute_import

from flask import Blueprint, render_template
from flask_security import login_required, current_user

root = Blueprint('root', __name__, static_folder='static', template_folder='templates', url_prefix='')


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

@root.route('/kidstars')
def login_page():
    return render_template('login.html')

@root.route('/dptest')
def dptest():
    return 'cool!'