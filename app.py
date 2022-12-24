from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from models import Users
from db import db_session

app = Flask(__name__)
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
api = Api(app)


class UsersSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()

class UsersQueryArgsSchema(ma.Schema):
    name = ma.fields.String()

blp = Blueprint('users', 'users', url_prefix="/users", description="Operations on pets")



@blp.route("/")
class Users_app(MethodView):
    @blp.arguments(UsersQueryArgsSchema, location="query")
    @blp.response(200, UsersSchema(many=True))
    def get(self, args):
        """List users"""
        return Users_app.get(filters=args)

api.register_blueprint(blp)
app.run()