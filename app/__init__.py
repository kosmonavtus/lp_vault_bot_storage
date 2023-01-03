#from app.db import Base
from flask import Flask
#from flask import request
#from app.classes import AppUsers, AppSecret
#from werkzeug.exceptions import BadRequestKeyError
import toml
from app.user.views import blueprint as user_blueprint
from app.secret.views import blueprint as sec_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_file("./config.toml", load=toml.load)
    #
    # Тут должен быть инит базы.
    # Не понял как инитнуть базу из апп.
    #
    app.register_blueprint(user_blueprint)
    app.register_blueprint(sec_blueprint)
    return app

if __name__ == "__main__":
    create_app(debug=True)

# Только из корня flask  --debug run