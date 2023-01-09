from flask import Blueprint, render_template


# Создаем главную страницу
bluprint = Blueprint('index', __name__)


@bluprint.route('/')
@bluprint.route('/index')
def index():
    return render_template('index.html')
