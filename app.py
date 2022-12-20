from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from models import Users
from db import db_session


def create_user(name, login, password):
    user = Users(name=name, login=login, password=password)
    db_session.add(user)
    db_session.commit()
    return f'maybe a user has been created {name}'

if __name__ == "__main__":
    create_user('test_user', 'test_login', 'test_password')

'''
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

class Login_pasword(Secert):
    def __init__(self, id, secret_id, secret_name, create_time, owner_id, secret_type,login,password,adress) -> None:
        super().__init__(id, secret_name, create_time, owner_id)
        self.secret_id = secret_id
        self.secret_type = secret_type
        self.login = login
        self.password = password
        self.adress = adress
    pass


class Users:
    def __init__(self, id,name,email,password,status) -> None:
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.status = status
    def create_user():
        pass
    def delete_user():
        pass
    def show_user():
        pass

'''
