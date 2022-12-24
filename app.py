from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from model import Users
from db import db_session









class AppSecert:
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

class AppLoginPasword(AppSecert):
    def __init__(self, id, name, user_id, sycret_type, status) -> None:
        super().__init__(id, name, user_id, sycret_type, status)
        
    pass


class AppUsers:
    def __init__(self, name,login,password,status=1) -> None:
        self.name = name
        self.login = login
        self.password = password
        self.status = status
    def create_user(self):
        user = Users(name=self.name, login=self.login, password=self.password)
        db_session.add(user)
        db_session.commit()
        return user.id
    def delete_user():
        pass
    def get_user(slef):
        user = Users.query.first()
        print(user)
        
        

if __name__ == "__main__":
    #создание полозователя работает
    Vasia = AppUsers(name='Vasya', login='Vasya', password='Vasya')
    #print(Vasia.create_user())
    Vasia.get_user()
