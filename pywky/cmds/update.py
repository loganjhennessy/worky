from click import argument, command, option

from pywky.db.models import Project
from pywky.db.session import make_session


@command()
@argument('name')
@option('-n', '--nickname')
@option('-d', '--directory')
@option('-i', '--ide-executable')
@option('-s', '--status')
def update(name, nickname, directory, ide_executable, status):
    """Update an existing project."""
    session = make_session()

    update = dict()
    if nickname:
        update[Project.name] = nickname
    if directory:
        update[Project.directory] = directory
    if ide_executable:
        update[Project.ide_exec] = ide_executable
    if status:
        update[Project.status] = status

    session.query(Project).filter(Project.name == name).\
        update(update, synchronize_session=False)
