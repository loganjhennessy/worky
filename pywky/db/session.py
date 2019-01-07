from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pywky.db.models import Base

engine = create_engine('sqlite:///worky_dev.db')
Base.metadata.bind = engine


def make_session():
    """Creates a session using the db config values for use by the endpoints.

    TODO: Look into making this a generator

    :return:
    """
    DBSession = sessionmaker(bind=engine)
    return DBSession()
