from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from db import Base, engine


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    login = Column(String(170), unique=True)
    password = Column(String(170))
    status = Column(bool)

    def __repr__(self) -> str:
        return f'User {self.id}, {self.name}, {self.login}'

class Secrets(Base):
    __tablename__ = "secrets"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    user_id = Column(Integer, ForeignKey("users.id"))
    sycret_type = Column(Integer, ForeignKey("secret_type.id"))
    status = Column(int)

    def __repr__(self) -> str:
        return f'secrets {self.id}, {self.name}, {self.status}'

class Secret_type(Base):
    __tablename__ = "secret_type"
    id = Column(Integer, primary_key=True)
    sycret_store_type = Column(Integer)

    def __repr__(self) -> str:
        return f'Secret_type {self.id}, {self.sycret_store_type}'

class login_password(Base):
    __tablename__ = "login_password"
    id = Column(Integer, primary_key=True)
    sycret_store_type = Column(Integer, ForeignKey("secret_type.sycret_store_type"))
    login = Column(String(1024))
    password = Column(String(2048))
    address = Column(String(256))
    create_date = Column(DateTime(timezone=True), default=func.now())
    descripton = Column(String(2048))

    def __repr__(self) -> str:
        return f'login_password {self.id}, {self.login}, {self.sycret_store_type}'



    



    def __repr__(self) -> str:
        return f'User {self.id}, {self.name}, {self.login}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
