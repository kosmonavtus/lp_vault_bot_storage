from flask import Flask
from flask import request
from classes import AppUsers, AppSecret


app = Flask(__name__)


@app.route("/uers", methods=['GET'])
def get_user():
    try:
        user_id = request.args.get('user_id')
        return AppUsers.get_user(user_id)
    except (ValueError, TypeError):
        return f'prequired parameter is user id'

@app.route("/secret", methods=['GET'])
def get_secret():
    try:    
        secret_id = request.args.get('secret_id')
        return AppSecret.get_secret(secret_id)
    except (ValueError, TypeError):
        return f'prequired parameter is secret id'

if __name__ == "__main__":
    app.run(debug=True)
