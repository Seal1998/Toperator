from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.engine import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    chat_id = Column(Integer, ForeignKey('chat.id'))
    chat = relationship('Chat', back_populates='posts')