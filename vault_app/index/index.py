# Код роутов
from flask import Blueprint, render_template


bluprint = Blueprint('index', __name__)


@bluprint.route('/')
@bluprint.route('/index')
def index():
    title = 'Home'
    user = {'username': 'miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Poland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Yasou'},
            'body': 'Death is like the wind, always by my side!'
        },
    ]
    return render_template('index.html', title=title, user=user, posts=posts)
