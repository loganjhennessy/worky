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
def list_projects(show_all):
    """List all projects.

    \f
    By default, inactive projects are hidden.
    """
    session = make_session()
    projects = session.query(Project).all()
    echo(Project.repr_header())
    for project in projects:
        echo(project)
