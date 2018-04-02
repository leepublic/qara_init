from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from common.db import Base


class User(Base):
    __tablename__ = 'qara_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime)
