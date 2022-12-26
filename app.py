from flask import Flask
from flask import request
from classes import AppUsers, AppSecret


app = Flask(__name__)


@app.route("/users", methods=['GET'])
def get_user():
        user_id = request.args.get('user_id')
        result = AppUsers.get_user(user_id)
        return result
    # AppUsers.get_user(user_id)

@app.route("/secret", methods=['GET'])
def get_secret():
    try:    
        secret_id = request.args.get('secret_id')
        return AppSecret.get_secret(secret_id)
    except (ValueError, TypeError):
        return f'prequired parameter is secret id'

if __name__ == "__main__":
    app.run(debug=True)
