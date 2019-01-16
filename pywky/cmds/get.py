from click import argument, command, echo, option

from pywky.db.models import Project
from pywky.db.session import make_session


@command()
@argument('name')
def get(name):
    """Retrieve an existing project.

    Arguments:

        NAME -- the name of the project to get
    """
    session = make_session()
    project = session.query(Project).filter(Project.name == name).all()

    if len(project) > 1:
        echo('Wat?')

    echo(project[0])