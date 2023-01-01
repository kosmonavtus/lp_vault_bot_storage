from db_model import Users, Secrets
from db import db_session
# Методом науного тыка нашел что exc - это исключения, 
# Есть какойто "нормальный" способ понять где в коде либы описаны исключения?
# Есть ли какоето соглашение которое говорит модуль с исключениями называем "вот так"?.
from sqlalchemy import exc

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
        try:
            q_result = Secrets.query.filter(Secrets.id == secret_id)
            return q_result.all()
        except (exc.DataError):
            return f'incorrect parameter secret_id: {secret_id}'
        except (exc.InternalError):
            return f'I dont understand why, but this sqlalchemy.exc.InternalError'
        except (exc.TimeoutError):
            return f'looks like your database ran away'
        except:
            return f'something else broke'
        # Вот этот код про обработку экспешенов дублируется.
        # Как то можно это во что то "завернуть" чтобы не дублировать? 


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
    def get_user(cls, user_id: int) -> str:
        try:
            q_result = Users.query.filter(Users.id == user_id)
            print(type(q_result.all()))
            return q_result.all()
            #return 'i am work!'
        except (exc.DataError):
            return f'incorrect parameter user_id: {user_id}'
        except (exc.InternalError):
            return f'I dont understand why, but this sqlalchemy.exc.InternalError'
        except (exc.TimeoutError):
            return f'looks like your database ran away'
        except:
            return f'something else broke'


            

    def delete_user(self):
        pass

if __name__ == "__main__":
    print((AppUsers.get_user(19)))
    #print((AppUsers.get_user(20)))
    #print((AppUsers.get_user('asdasdas')))
    #print((AppUsers.get_user(21)))
    # Разобрался с перехватом исключений от алхимии вроде бы.
    # Но так и не понял почему 4ый принт вовзвращает исключение sqlalchemy.exc.InternalError
    # Мое предположение я не понимаю как работаетют методы классса и все дело в этом.
    # Если один раз метод вызывается с ошибкой то возвращается sqlalchemy.exc.InternalError с любым параметром.