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
fmtstr = '''\
Id:               {id}
Name:             {name}
Nickname:         {nickname}
Repo:             {repo}
Branch:           {branch}
Ide Executable:   {ide_exec}
Status:           {status}
Scratch Dir:      {scratch_dir}
Ticket:           {ticket}\
'''
fmtstr_abbr = '{:10}{:8}  {:>36}'


class Project(Base):
    __tablename__ = 'project'
    id = Column(Text, primary_key=True, default=generate_uuid())
    name = Column(Text, unique=True)
    nickname = Column(Text)
    repo = Column(Text)
    ide_exec = Column(Text)
    status = Column(Text)
    scratch_dir = Column(Text)
    ticket = Column(Text)
    branch = Column(Text)

    def __repr__(self):
        return fmtstr.format(
            id=self.id,
            name=self.name,
            nickname=self.nickname,
            repo=self.repo,
            branch=self.branch,
            ide_exec=self.ide_exec,
            status=self.status,
            scratch_dir=self.scratch_dir,
            ticket=self.ticket
        )

    def repr_abbr(self):
        return fmtstr_abbr.format(self.name, self.status, self.id)

    @staticmethod
    def repr_abbr_header():
        return fmtstr_abbr.format('Name', 'Status', 'Id')
