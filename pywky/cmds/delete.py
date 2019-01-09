from click import argument, command

from pywky.db.models import Project
from pywky.db.session import make_session

@command()
@argument('name')
def delete(name):
    """Delete an existing project.

    Arguments:

        NAME -- the name of the project to delete
    """
    session = make_session()
    session.query(Project).filter(Project.name == name).\
        delete(synchronize_session=False)
    session.commit()
