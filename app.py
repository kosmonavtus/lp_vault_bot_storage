from flask import Flask
from flask import request
from classes import AppUsers, AppSecret


app = Flask(__name__)


@app.route("/user", methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    if isinstance(user_id, int):
        return AppUsers.get_user(user_id)
    else:
        return f'Parameter error'


@app.route("/secret", methods=['GET'])
def get_secret():
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