from click import command, echo, option

from pywky.db.models import Project
from pywky.db.session import make_session


@command('list')
@option(
    '-a',
    '--show-all',
    is_flag=True,
    default=False,
    help='Show all projects, including inactive.'
)
@option(
    '-h',
    '--show-headers',
    is_flag=True,
    default=False,
    help='Hide header for the list, showing the data only.'
)
def list_projects(show_all, show_headers):
    """List all projects.

    \f
    By default, inactive projects are hidden.
    """
    session = make_session()
    projects = session.query(Project).all()

    if show_headers:
        echo(Project.repr_header())

    for project in projects:
        echo(project)
