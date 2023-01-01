from db_model import Users, Secrets
from db import db_session


class AppSecret:
    def __init__(self, name: str, user_id: int, sycret_type: int) -> None:
        self.name = name
        self.user_id = user_id
        self.sycret_type = sycret_type

    def create_secret(self):
        secret = Secrets(
                        name=self.name,
                        user_id=self.user_id,
                        sycret_type=self.sycret_type,
                        )
        db_session.add(secret)
        db_session.commit()
        return secret.id

    @classmethod
    def get_secret(self, secret_id: int) -> str:
        q_result = Secrets.query.filter(Secrets.id == secret_id)
        for _ in q_result:
            return f'{_}'

    def delete_secret():
        pass


class AppUsers:
    def __init__(self, name: str, login: str, password: str, status: bool = True) -> None:
        self.name = name
        self.login = login
        self.password = password
        self.status = status

    def create_user(self) -> int:
        user = Users(
                    name=self.name,
                    login=self.login,
                    password=self.password
                    )
        db_session.add(user)
        db_session.commit()
        return user.id

    @classmethod
    def get_user(slef, user_id: int) -> str:
        try:
            q_result = Users.query.filter(Users.id == user_id)
            # не понимаю как получить результат без for _ 
            # если возвращать q_result то возвращается запрос.
            #for _ in q_result:
            #    return f'{_}'
            return q_result.all()
        except:
            # не понимаю каой тип исключения тут прилетает и как перехватывать именно гего?
            return False
            # А можно вызывать самому Rise TypeError вместо return False?
            # Или нужно возвращать фалс ? 

            

    def delete_user(self):
        pass

if __name__ == "__main__":
    # Как так выходит если делать два принта подряд 
    # Один с кривым парметром другой с правильным
    # то оба возвращают False ? 
    # Они както в одну транзацию в лезают оба?
    #   print(AppUsers.get_user('asdasdas'))
    print(AppUsers.get_user(10))