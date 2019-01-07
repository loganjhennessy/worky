from sqlalchemy import create_engine

from pywky.db.models import Base

engine = create_engine('sqlite:///worky_dev.db')
Base.metadata.bind = engine
