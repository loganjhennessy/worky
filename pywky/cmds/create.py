from click import argument, command, echo, option
from sqlalchemy.exc import IntegrityError

from pywky.db.models import Project
from pywky.db.session import make_session


@command()
@argument('name')
@option('-n', '--nickname')
@option('-r', '--repository')
@option('-i', '--ide-executable')
def create(name, nickname, repository, ide_executable):
    """Create a new project.

    \b
    Required argument(s):
      NAME: Name for the project

    \f
    :param name: Name for the project
    :param nickname: Short name for the project
    :param directory: Where the project is located
    :param ide_executable: What to launch when opening the project
    """
    session = make_session()
    project = Project(
        name=name,
        nickname=nickname,
        repo=repository,
        ide_exec=ide_executable,
        status='ACTIVE'
    )

    try:
        session.add(project)
        session.commit()
    except IntegrityError as e:
        echo(f'Could not create a project with name: {name}')
        echo('\n    A project with that name already exists.')
