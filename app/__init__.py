from flask import Flask
from flask import request
from app.classes import AppUsers, AppSecret
from werkzeug.exceptions import BadRequestKeyError
import toml


def create_app():
    app = Flask(__name__)
    app.config.from_file("./config.toml", load=toml.load)

    @app.route("/user", methods=['GET'])
    def user():
        print(app.config)
        try:
            if request.args['user_id'].isdigit():
                user_id = int(request.args['user_id'])
                return str(AppUsers.get_user(user_id))
            else:
                return f'Error {user_id} parametr not int'
        except (BadRequestKeyError):
            return f'user_id parameter was not received'


    @app.route("/secret", methods=['GET'])
    def secret():
        try:
            secret_id = request.args.get('secret_id')
            if isinstance(secret_id, int):
                return AppSecret.get_secret(secret_id)
            else:
                return f'Error {secret_id} parametr not int'
        except (BadRequestKeyError):
            return f'secret_id parameter was not received'


    @app.route("/add_user", methods=['POST'])
    def add_user():
        pass

    return app

if __name__ == "__main__":
    create_app(debug=True)
# а почему оно отсюда вот таким образом больше не запускается ? 
# Только из корня flask  --debug run