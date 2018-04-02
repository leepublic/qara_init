from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, BLOB
from sqlalchemy.orm import relationship, backref

from common.db import Base, db_session as conn


class User(Base):
    __tablename__ = 'qara_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime)


class FlaskSession(Base):
    __tablename__ = 'flask_session'

    sid = Column(String, primary_key=True)
    value = Column(BLOB)

    @classmethod
    def change(cls, sid, value):
        rec = conn.query(cls).filter(cls.sid == sid).first()
        if not rec:
            rec = cls()
            rec.sid = sid
        rec.value = value
        return rec
