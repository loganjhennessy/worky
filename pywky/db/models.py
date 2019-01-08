import uuid

from click import echo
from sqlalchemy import Boolean, Column, Text
from sqlalchemy.ext.declarative import declarative_base


def generate_uuid():
    """Generate a unique identifier for a database row.

    Lifted from:
        https://stackoverflow.com/questions/183042/\
        how-can-i-use-uuids-in-sqlalchemy
    """
    return str(uuid.uuid4())


Base = declarative_base()
fmtstr = '{:10}{:6}  {:>36}'

class Project(Base):
    __tablename__ = 'project'
    id = Column(Text, primary_key=True, default=generate_uuid())
    name = Column(Text)
    nickname = Column(Text)
    directory = Column(Text)
    ide_exec = Column(Text)
    active = Column(Boolean)

    def __repr__(self):
        return fmtstr.format(self.name, self.active, self.id)

    @staticmethod
    def repr_header():
        return fmtstr.format('Name', 'Active', 'Id')
