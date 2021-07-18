from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///botdb.sqlite', echo=False)
Session = sessionmaker(bind=engine)

db = Session()

Base = declarative_base()