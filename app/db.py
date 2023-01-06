from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import toml

config = toml.load('app/config.toml')

engine = create_engine(config['CONNECTION_STRING'])
Base = declarative_base()

db_session = scoped_session(sessionmaker(bind=engine))


Base.query = db_session.query_property()
