from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from app.db import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(170))
    login = Column(String(170), unique=True)
    password = Column(String(170))
    status = Column(Boolean, default=True)

    def __repr__(self) -> dict:
        return f' {self.id}, {self.name}, {self.login}, {self.password}, {self.status}'
