from flask import Flask
from flask import request
from classes import AppUsers, AppSecret
from werkzeug.exceptions import BadRequestKeyError


app = Flask(__name__)


@app.route("/user", methods=['GET'])
def user():
    try:
        if request.args['user_id'].isdigit():
            user_id = int(request.args['user_id'])
            return str(AppUsers.get_user(user_id))
        else:
            return f'Parameter error {user_id}'
    except (BadRequestKeyError):
        return f'user_id parameter was not received'




@app.route("/secret", methods=['GET'])
def secret():
    secret_id = request.args.get('secret_id')
    if isinstance(secret_id, int):
        return AppSecret.get_secret(secret_id)
    else:
        return f'Parameter error'

@app.route("/add_user", methods=['POST'])
def add_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)

#  return AppUsers.get_user(request.args.get('user_id'))