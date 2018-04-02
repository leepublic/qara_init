import os
import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

print "env : "+str(os.environ.get('DB_NAME'))


db_connection_string = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_NAME
)

engine = create_engine(db_connection_string, echo=True, convert_unicode=False)
db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import users.models
    Base.metadata.create_all(bind=engine)
