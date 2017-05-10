from __future__ import absolute_import

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_security import login_required, current_user

from app import db
from kidstars.models import Child
from kidstars.forms import ChildForm

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

@login_required
@root.route('/child', methods=['POST', 'GET'])
def child_add():
    child_form = ChildForm(request.form)
    if request.method == 'POST' and child_form.validate():
        child = Child(name=child_form.name,
                      birth_date=child_form.birth_date)
        db.session.add(child)
        db.session.commit()
        flash('Child {} registered!'.format(child_form.name))
        return redirect(url_for('child', {'child_id': child.id}))
    return render_template('forms/child_form.html', form=child_form)