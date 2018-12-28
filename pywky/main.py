"""main.py

    Entry-point for pywky, an app that manages dev work.
"""
from pywky.lib.args import args
from pywky.core import cmds



def main():
    cmd = getattr(cmds, args.cmd)
    if args.cmd == 'create':
        pass
    elif args.cmd == 'goto':
        pass
    elif args.cmd == 'update':
        pass
    elif args.cmd == 'delete':
        pass
    else:
        raise Exception('This should never happen')


if __name__ == '__main__':
    main()
