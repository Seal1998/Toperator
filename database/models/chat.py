from sqlalchemy import Column, Integer, String
from database.engine import Base, db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    telegram_id = Column(Integer)
    type = Column(String(length=20))

    accounts = relationship('Account', back_populates='chat')
    posts = relationship('Post', back_populates='chat')

    @classmethod
    def add(cls, name, tid):
        if cls.get_by_tid(tid):
            return False #if already exists - do nothing
        else:
            new_chat = cls(name=name, telegram_id=tid)
            db.add(new_chat)
            db.commit()
            return new_chat

    @classmethod
    def get_by_tid(cls, tid):
        chat = db.query(cls).filter(cls.telegram_id==tid).first()
        if chat is None:
            return False
        else:
            return chat

    def __repr__(self):
        return self.name