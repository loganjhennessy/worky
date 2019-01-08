from sqlalchemy import create_engine

from pywky.db.models import Base, Project


def create_db():
    engine = create_engine('sqlite:///worky_dev.db')
    Base.metadata.create_all(engine)

def recreate_db():
    engine = create_engine('sqlite:///worky_dev.db')
    Project.__table__.drop(engine)
    Base.metadata.drop_all(bind=engine, tables=[Project.__table__])
    Base.metadata.create_all(engine)
