from werkzeug.exceptions import BadRequestKeyError
from app.classes import AppRepo
from flask import request
from flask import Blueprint

blueprint = Blueprint('sec',__name__, url_prefix='/sec')

@blueprint.route("/secret", methods=['GET'])
def secret():
    try:
        secret_id = request.args.get('secret_id')
        if secret_id.isdigit():
            query_obj = AppRepo.get_secret(secret_id)
            return str(query_obj.all())
        else:
            return f'Error {secret_id} parametr not int'
    except (BadRequestKeyError):
        return f'secret_id parameter was not received'

@blueprint.route("/add_secret", methods=['POST'])
def add_secret():
    try:
        request_data = request.get_json()
        #  Тут бы хорошо проверить тайпдиктом что пришло то что нужно на вход
        #  А еще бы наверное хорошо проверять самому приложениею что userid в базе существует а не базу мучать.
        secret = AppRepo(name=request_data['name'], user_id=request_data['user_id'], secret_type=request_data['secret_type'])
        result = secret.create_secret()
        return str(result)
    except (BadRequestKeyError):
        return f'{request.get_data} parameter was not received'



@blueprint.route("/delete_secret", methods=['POST'])
def del_secret():
    try:
        request_data = request.get_json()
        secret_id_int = int(request_data['secret_id'])
        result = AppRepo.delete_secret(secret_id_int)
        return str(result)
    except (BadRequestKeyError):
        return f'{request.get_data} parameter was not received'
