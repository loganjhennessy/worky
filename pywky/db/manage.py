from sqlalchemy import create_engine

from pywky.db.models import Base


def create_db():
    engine = create_engine('sqlite:///worky_dev.db')
    Base.metadata.create_all(engine)
