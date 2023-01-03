from db_model import Users
from db import db_session


def get_user_data(name: str) -> str:
    # получаем данные пользователя (переменная name) из БД
    
    user_data = db_session.query(
        Users.login,
        Users.password
    ).filter(Users.name == name).all()
    for login, password in user_data:
        print(f"User: {name}, login: {login}, password: {password}")


if __name__ == "__main__":
    get_user_data("Victoria Smith")
