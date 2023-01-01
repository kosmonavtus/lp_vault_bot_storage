from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from db import Base, engine


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    login = Column(String(170), unique=True)
    password = Column(String(170))
    status = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f' {self.id}, {self.name}, {self.login}, {self.password} {self.status}'


class Secrets(Base):
    __tablename__ = "secrets"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    user_id = Column(Integer, ForeignKey("users.id"))
    sycret_type = Column(Integer, ForeignKey("secret_type.id"))

    def __repr__(self) -> str:
        return f'{self.id}, {self.name}, {self.user_id}, {self.sycret_type}'

# Пока незнаю на что хватит вермени.
# Можно хранит отчеты данные пользователя в выдолбленной в маналитном SQL структуре.
# А можно дать свободу и хранить какието обстрактные key:value словари и пусть что хочт то и хранит.


class SecretType(Base):
    __tablename__ = "secret_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    sycret_store_type = Column(Integer)

    def __repr__(self) -> str:
        return f'Secret_type {self.id}, {self.sycret_store_type}'


# Подразумивается что могут быть отедльне разные таблицы для рахных видов данных.
# По этому есть отедльная табличка "login_password"
# Для логин / паролей одни, для RSA другие, для SSL X.509 третие.


class login_password(Base):
    __tablename__ = "login_password"
    id = Column(Integer, primary_key=True)
    sycret_store_type = Column(Integer, ForeignKey("secret_type.id"))
    login = Column(String(1024))
    password = Column(String(2048))
    address = Column(String(256))
    create_date = Column(DateTime(timezone=True), default=func.now())
    descripton = Column(String(2048))

    def __repr__(self) -> str:
        return (f'{self.id}, {self.sycret_store_type}, {self.login},'
                f'{self.password}, {self.address}, {self.create_date}, {self.descripton}')


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

