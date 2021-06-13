from database.engine import Base, engine
from database.models import *

if __name__ == '__main__':
    Base.metadata.create_all(engine)