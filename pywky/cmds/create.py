from click import argument, command, option

from pywky.db.models import Project
from pywky.db.session import make_session


@command()
@argument('name')
@option('-n', '--nickname')
@option('-d', '--directory')
@option('-i', '--ide-executable')
def create(name, nickname, directory, ide_executable):
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
        directory=directory,
        ide_exec=ide_executable,
        active=True
    )
    session.add(project)
    session.commit()
