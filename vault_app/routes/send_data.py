from flask import Blueprint, render_template
from forms import SendData


# Создаем форму ввода пользователя, для которого необходимо вывести секреты
bluprint = Blueprint('send_data', __name__)


@bluprint.route('/send_data')
def send_data():
    form = SendData()
    title = 'Get secret!'
    return render_template('send_data.html', title=title, form=form)
