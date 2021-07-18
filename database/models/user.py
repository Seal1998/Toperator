from sqlalchemy import Column, Integer, String
from database.engine import Base, db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    telegram_id = Column(Integer)
    accounts = relationship('Account', back_populates='user')

    @classmethod
    def add(cls, name, tid):
        new_user = cls(name=name, telegram_id=tid)
        db.add(new_user)
        db.commit()
        return new_user

    @classmethod
    def get_by_tid(cls, tid):
        user = db.query(cls).filter(cls.telegram_id==tid).first()
        if user is None:
            return False
        else:
            return user

    def __repr__(self):
        return self.name
