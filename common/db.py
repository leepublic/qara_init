import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

db_connection_string = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
   	Config.DB_USER,
    Config.DB_PASSWORD,
    Config.DB_HOST,
    Config.DB_NAME
)

engine = create_engine(db_connection_string, echo=False, convert_unicode=False)
db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import accounts.models
    Base.metadata.create_all(bind=engine)
