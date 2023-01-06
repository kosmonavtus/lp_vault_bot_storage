from app.secret.models import Secrets
from app.user.models import Users
from app.db import db_session
from sqlalchemy import exc, orm
from sqlalchemy import delete


class AppSecret:
    def __init__(self, name: str, user_id: int, secret_type: int) -> None:
        self.name = name
        self.user_id = user_id
        self.secret_type = secret_type

    def create_secret(self):
        secret = Secrets(
                        name=self.name,
                        user_id=self.user_id,
                        secret_type=self.secret_type,
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
    def get_secret(self, secret_id: int) -> orm.query.Query:
        try:
            q_result = Secrets.query.filter(Secrets.id == secret_id)
            return q_result
        except (exc.DataError):
            return f'incorrect parameter secret_id: {secret_id}'
        except (exc.InternalError):
            return f'I dont understand why, but this sqlalchemy.exc.InternalError'
        except (exc.TimeoutError):
            return f'looks like your database ran away'
        except (exc.OperationalError):
            return f'Is the server running on that host and accepting TCP/IP connections?'
        except:
            return False

    @classmethod
    def delete_secret(self, secret_id: int):
        try:
            stm = delete(Secrets).where(Secrets.id == secret_id)
            db_session.execute(stm)
            db_session.commit()
            return True
        except:
            return False


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
    def delete_user(self, user_id: int)-> bool:
        try:
            stm = delete(Users).where(Users.id == user_id)
            db_session.execute(stm)
            db_session.commit()
            return True
        except:
            return False
        

if __name__ == "__main__":
    #print((AppUsers.get_user(19)))
    #print((AppUsers.get_user(20)))
    #print((AppUsers.get_user('asdasdas')))
    #print((AppUsers.get_user(21)))
    # Разобрался с перехватом исключений от алхимии вроде бы.
    # Но так и не понял почему 4ый принт вовзвращает исключение sqlalchemy.exc.InternalError
    # Мое предположение я не понимаю как работаетют методы классса и все дело в этом.
    # Если один раз метод вызывается с ошибкой то возвращается sqlalchemy.exc.InternalError с любым параметром.

    # Этот код для отладки не работает, после перехода к bluerprint views/model.
    # Пока не понимаю в каком месте проекта правильно такие костыли для отдладки разхмещать.

    pass