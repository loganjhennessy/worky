from click import command, option


@command('list')
@option(
    '--show-inactive',
    is_flag=True,
    default=False,
    help='Show inactive projects.'
)
def list_projects(show_inactive):
    """List all projects.

    By default, inactive projects are hidden.
    """
    pass
