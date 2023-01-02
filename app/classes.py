from .db_model import Users, Secrets
from .db import db_session
# Методом науного тыка нашел что exc - это исключения в sqlalchemy, 
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
        try:
            db_session.add(secret)
            db_session.commit()
        except (exc.IntegrityError):
            return f'Tried made insert with wrong data {secret}'
        except (exc.OperationalError):
            return f'Is the server running on that host and accepting TCP/IP connections?'
        except Exception as e:
            return(e)
        return True


    @classmethod
    def get_secret(self, secret_id: int) -> str:
        try:
            q_result = Secrets.query.filter(Secrets.id == secret_id)
            return q_result.all()
            # Тут навернео не плохо было бы возврашать обьект и дальше с ним разбираться в других функциях.
            # А а не тупо строку сразу.
        except (exc.DataError):
            return f'incorrect parameter secret_id: {secret_id}'
        except (exc.InternalError):
            return f'I dont understand why, but this sqlalchemy.exc.InternalError'
        except (exc.TimeoutError):
            return f'looks like your database ran away'
        except (exc.OperationalError):
            return f'Is the server running on that host and accepting TCP/IP connections?'
        except Exception as e:
            return(e)
        # Вот этот код про обработку экспешенов дублируется.
        # Как то можно это во что то "завернуть" чтобы не дублировать?


    def delete_secret(self, secret_id):
        try:
            user_for_delete = db_session.get(Secrets, secret_id)
            db_session.delete(user_for_delete)
            db_session.commit()
            return True
        except Exception as e:
            return(e)


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
        try:
            db_session.add(user)
            db_session.commit()
        except (exc.IntegrityError):
            return f'Tried made insert with wrong data {user}'
        except (exc.OperationalError):
            return f'Is the server running on that host and accepting TCP/IP connections?'
        except Exception as e:
            return(e)
        return True
        #  Я вовзвращю строчки с описаниями потому что тупой и мне так проще отладить.
        #  Но Сдравый смысл мне подсказывает что что то тут не так.
        #  Не до конца понимаю что тут надо возвращать назад что бы программа себя "адекватно" вела.
        #  А не "взрывавалась" в случае ошибки.
    @classmethod
    def get_user(cls, user_id: int) -> str:
        try:
            q_result = Users.query.filter(Users.id == user_id)
            return q_result.all()
        except (exc.DataError):
            return f'incorrect parameter user_id: {user_id}'
        except (exc.InternalError):
            return f'I dont understand why, but this sqlalchemy.exc.InternalError'
        except (exc.TimeoutError):
            return f'looks like your database ran away'
        except (exc.OperationalError):
            return f'Is the server running on that host and accepting TCP/IP connections?'
        except Exception as e:
            return(e)


    @classmethod
    def delete_user(self, user_id):
        try:
            # Хочу удолть пользователя не делая перед этим зарпоса в базу, не понимаю как это сделать.
            user_for_delete = db_session.get(Users, user_id)
            db_session.delete(user_for_delete)
            db_session.commit()
            return True
        except Exception as e:
            return(e)
        

if __name__ == "__main__":
    print((AppUsers.get_user(19)))
    print((AppUsers.get_user(20)))
    print((AppUsers.get_user('asdasdas')))
    print((AppUsers.get_user(21)))
    # Разобрался с перехватом исключений от алхимии вроде бы.
    # Но так и не понял почему 4ый принт вовзвращает исключение sqlalchemy.exc.InternalError
    # Мое предположение я не понимаю как работаетют методы классса и все дело в этом.
    # Если один раз метод вызывается с ошибкой то возвращается sqlalchemy.exc.InternalError с любым параметром.