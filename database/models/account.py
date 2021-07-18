from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database.engine import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    chat_id = Column(Integer, ForeignKey('chat.id'))
    user = relationship('User', back_populates='accounts')
    chat = relationship('Chat', back_populates='accounts')