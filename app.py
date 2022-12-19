from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort

class Secert:
    def __init__(self,id,secret_name,create_time,owner_id) -> None:
        self.id = id
        self.secret_name = secret_name
        self.create_time = create_time
        self.owner_id = owner_id
    def write():
        pass
    def get():
        pass
    def edit():
        pass

class Login_pasword(secert):
    def __init__(self, id, secret_name, create_time, owner_id, secret_type,login,password,adress) -> None:
        super().__init__(id, secret_name, create_time, owner_id)
        self.secret_type = secret_type
        self.login = login
        self.password = password
        self.adress = adress
    pass


class Users:
    def __init__(self, id,name,email,password) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        pass
    def create_user():
        pass
    def delete_user():
        pass
    def show_user():
        pass