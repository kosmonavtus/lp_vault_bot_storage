from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from .db import Base, engine




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
