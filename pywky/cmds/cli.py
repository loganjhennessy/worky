from click import group

from .create import create
from .retrieve import retrieve
from .update import update
from .list_projects import list_projects
from .delete import delete

@group()
def cli():
    pass

cli.add_command(create)
cli.add_command(update)
cli.add_command(retrieve)
cli.add_command(list_projects)
cli.add_command(delete)
