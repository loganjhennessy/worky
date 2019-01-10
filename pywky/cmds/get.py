from click import argument, command, echo, option

from pywky.db.models import Project
from pywky.db.session import make_session


@command()
@argument('name')
@option(
    '-h',
    '--show-header',
    is_flag=True,
    default=False,
    help='Hide header for the list, showing the data only.'
)
def get(name, show_header):
    """Retrieve an existing project.

    Arguments:

        NAME -- the name of the project to get
    """
    session = make_session()
    project = session.query(Project).filter(Project.name == name).all()

    if show_header:
        echo(Project.repr_header())

    if len(project) > 1:
        echo('Wat?')

    echo(project[0])