from click import argument, command


@command()
@argument('name')
def delete():
    """Delete an existing project.

    Arguments:

        NAME -- the name of the project to delete
    """
    pass
