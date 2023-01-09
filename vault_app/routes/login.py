from flask import Blueprint, render_template
from forms import LoginForm


bluprint = Blueprint('login', __name__)


@bluprint.route('/login')
def login():
    form = LoginForm()
    title = 'Sign in'
    return render_template('login.html', title=title, form=form)
