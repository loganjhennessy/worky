import uuid

from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base


def generate_uuid():
    """Generate a unique identifier for a database row.

    Lifted from:
        https://stackoverflow.com/questions/183042/\
        how-can-i-use-uuids-in-sqlalchemy
    """
    return str(uuid.uuid4())


Base = declarative_base()
fmtstr = '{:36}  {:10}  {:8}  {:60}  {:10}  {:8}'
fmtstr_abbr = '{:10}{:8}  {:>36}'


class Project(Base):
    __tablename__ = 'project'
    id = Column(Text, primary_key=True, default=generate_uuid())
    name = Column(Text)
    nickname = Column(Text)
    directory = Column(Text)
    ide_exec = Column(Text)
    status = Column(Text)

    def __repr__(self):
        return fmtstr.format(
            self.id,
            self.name,
            self.nickname,
            self.directory,
            self.ide_exec,
            self.status
        )

    def repr_abbr(self):
        return fmtstr_abbr.format(self.name, self.status, self.id)

    @staticmethod
    def repr_abbr_header():
        return fmtstr_abbr.format('Name', 'Status', 'Id')

    @staticmethod
    def repr_header():
        return fmtstr.format(
            'Id',
            'Name',
            'Nickname',
            'Directory',
            'Ide Exec',
            'Status'
        )
