from werkzeug.exceptions import BadRequestKeyError
from app.classes import AppUsers
from flask import request
from flask import Blueprint

# Имя модуля?
# Можно про ситсемную штуку __name___ поглубже рассказать?
#
# Вроде бы это системная переменная в которую залетает имя модуля.
# И она же используется для разбиения кода на модули.
# Но я слишком туп чтобы вместе все обрывки инфы связать )
# Как здесь работает __name__?
blueprint = Blueprint('user',__name__, url_prefix='/users')

@blueprint.route("/user", methods=['GET'])
def user():
    try:
        if request.args['user_id'].isdigit():
            user_id = int(request.args['user_id'])
            return str(AppUsers.get_user(user_id))
        else:
            return f'Error {user_id} parametr not int'
    except (BadRequestKeyError):
        return f'user_id parameter was not received'

@blueprint.route("/add_user", methods=['POST'])
def add_user():
    try: 
        request_data = request.get_json()
        user = AppUsers(name=request_data['name'], login=request_data['login'], password=request_data['password'])
        result_user_create = user.create_user()
        return str(result_user_create)
    except (BadRequestKeyError):
        return f'{request.get_data} parameter was not received'


# выглядит как какойто пиздец.
# Слишком сложно както по моему.
@blueprint.route("/delete_user", methods=['POST'])
def del_user():
    try:
        request_data = request.get_json()
        user_id_int = int(request_data['user_id'])
        result = AppUsers.delete_user(user_id_int)
        return str(result)
    except (BadRequestKeyError):
        return f'{request.get_data} parameter was not received'