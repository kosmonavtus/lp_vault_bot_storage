from flask import Flask
from flask import request
from classes import AppUsers, AppSecert


app = Flask(__name__)


@app.route("/uers", methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    return AppUsers.get_user(user_id)


@app.route("/secret", methods=['GET'])
def get_secret():
    secret_id = request.args.get('secret_id')
    return AppSecert.get_secrt(secret_id)

if __name__ == "__main__":
    app.run(debug=True)
