from sqlalchemy import Column, Integer, String
from database.engine import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Channel(Base):
    __tablename__ = 'channel'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    telegram_id = Column(Integer)

    accounts = relationship('Account', back_populates='channel')
    posts = relationship('Post', back_populates='channel')