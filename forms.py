from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Создаём классы веб-форм используя flask_wtf
# validators=[DataRequired()] проверяет не отправлено ли поле пустым


class LoginForm(FlaskForm):
    # Форма авторизации
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class SendData(FlaskForm):
    # Форма для ввода имени пользователя секреты которого необходимо вывести
    user = StringField('User', validators=[DataRequired()])
    submit = SubmitField('Send')
