from flask import Blueprint, flash, redirect, render_template, url_for
from forms import LoginForm


# Создаём форму ввода логина и пароля
bluprint = Blueprint('login', __name__)


@bluprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title = 'Sign in'
    if form.validate_on_submit:
        flash('Login requested for user {},\
            remember_me={}'.format(form.username.data, form.remember_me.data))
        redirect(url_for('index.index'))
    return render_template('login.html', title=title, form=form)
