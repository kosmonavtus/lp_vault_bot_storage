from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from models import Users
from db import db_session


class Secert:
    def __init__(self,id,name,user_id,sycret_type,status) -> None:
        self.id = id
        self.name = name
        self.user_id = user_id
        self.sycret_type = sycret_type
        self.status = status
    def write():
        pass
    def get():
        pass
    def edit():
        pass

class Login_pasword(Secert):
    def __init__(self, id, name, user_id, sycret_type, status) -> None:
        super().__init__(id, name, user_id, sycret_type, status)
        
    pass


class Users:
    def __init__(self, id,name,login,password,status) -> None:
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

def create_user(name, login, password):
    user = Users(name=name, login=login, password=password)
    db_session.add(user)
    db_session.commit()
    return f'maybe a user has been created {name}'

if __name__ == "__main__":
    create_user('test_user', 'test_login', 'test_password')