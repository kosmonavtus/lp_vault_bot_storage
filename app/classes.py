"""Defining the base classes of the application."""
from app.repositories.models import Repositories
from app.user.models import Users
from app.db import db_session
from sqlalchemy import exc, orm
from sqlalchemy import delete


class AppRepo:
    """The class describes the repository of secrets and methods of working with it."""

    def __init__(self, name: str, user_id: int, secret_type: int) -> None:
        """Вefine  basic parameters of the secret."""
        self.name = name
        self.user_id = user_id
        self.secret_type = secret_type

    @classmethod
    def get_secret(self, secret_id: int) -> orm.query.Query:
        """Get secret by ID."""
        try:
            q_result = Repositories.query.filter(Repositories.id == secret_id)
            return q_result
        except (exc.DataError, exc.InternalError, exc.OperationalError, exc.TimeoutError):
            return False

    @classmethod
    def delete_secret(self, secret_id: int) -> None:
        """Delete secret by ID."""
        try:
            stm = delete(Repositories).where(Repositories.id == secret_id)
            db_session.execute(stm)
            db_session.commit()
            return None
        except (exc.OperationalError, exc.TimeoutError):
            return 'Database error'

    def create_secret(self) -> None:
        """Write secret in the database."""
        secret = Repositories(
            name=self.name,
            user_id=self.user_id,
            ecret_type=self.secret_type)
        try:
            db_session.add(secret)
            db_session.commit()
        except (exc.IntegrityError, exc.OperationalError):
            return 'Database error'
        return None


class AppUsers:
    """Class interacts with users."""

    def __init__(self, name: str, login: str, password: str, status: bool = True) -> None:
        """Тут должен быть док стринг но я хз зачем и так все поятно."""
        self.name = name
        self.login = login
        self.password = password
        self.status = status

    @classmethod
    def get_user(cls, user_id: int) -> str:
        """Get user by ID from DB."""
        try:
            q_result = Users.query.filter(Users.id == user_id)
            return q_result.all()
        except (exc.DataError, exc.InternalError, exc.OperationalError, exc.TimeoutError):
            return 'Database error'

    @classmethod
    def delete_user(self, user_id: int) -> None:
        """Remove user by ID from DB."""
        try:
            stm = delete(Users).where(Users.id == user_id)
            db_session.execute(stm)
            db_session.commit()
            return None
        except (exc.TimeoutError):
            return 'Database error'

    def create_user(self) -> None:
        """Write user to DB ."""
        user = Users(
            name=self.name,
            login=self.login,
            password=self.password)
        try:
            db_session.add(user)
            db_session.commit()
        except (exc.IntegrityError):
            return f'Tried made insert with wrong data {user}'
        except (exc.OperationalError):
            return 'Is the server running on that host and accepting TCP/IP connections?'
        return True
