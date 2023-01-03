from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from app.db import Base


class Secrets(Base):
    __tablename__ = "secrets"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    user_id = Column(Integer, ForeignKey("users.id"))
    secret_type = Column(Integer, ForeignKey("secret_type.id"))

    def __repr__(self) -> str:
        return f'{self.id}, {self.name}, {self.user_id}, {self.secret_type}'


class SecretType(Base):
    __tablename__ = "secret_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    secret_store_type = Column(Integer)

    def __repr__(self) -> str:
        return f'Secret_type {self.id}, {self.secret_store_type}'