from click import argument, command


@command()
@argument('name')
def retrieve(name):
    """Retrieve an existing project.

    Arguments:

        NAME -- the name of the project to retrieve
    """
    pass
