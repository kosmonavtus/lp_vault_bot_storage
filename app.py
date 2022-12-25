from flask import Flask
from flask import request
from classes import AppUsers, AppSecert


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'palse for default content'


@app.route("/get_uers", methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    return AppUsers.get_user(user_id)


@app.route("/get_secret", methods=['GET'])
def get_secret():
    secret_id = request.args.get('secret_id')
    return AppSecert.get_secrt(secret_id)


app.run(debug=True)
