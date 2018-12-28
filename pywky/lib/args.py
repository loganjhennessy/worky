"""pywky.args

    Command-line argument parser for pywky.
"""
import argparse

parser = argparse.ArgumentParser(prog='pywky')
subparser = parser.add_subparsers()

create_p = subparser.add_parser('create', help='Create a new project')

retrieve_p = subparser.add_parser(
    'retrieve', help='Retrieve an existing project'
)
retrieve_p.add_argument('name', help='Name of the project to retrieve')

list_p = subparser.add_parser('list', help='List all projects')
list_p.add_argument('-a', '--all', help='Show inactive projects')

update = subparser.add_parser('update', help='Update an existing project')
delete = subparser.add_parser('delete', help='Delete a project')

args = parser.parse_args()
