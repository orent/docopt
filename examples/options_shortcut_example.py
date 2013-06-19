"""Example of program which uses [options] shortcut in pattern.

Usage:
  options_shortcut_example.py [options] <port>

Options:
  -h --help                show this help message and exit
  --version                show version and exit
  -n, --number N           use N as a number
  -t, --timeout TIMEOUT    set timeout TIMEOUT seconds
  --apply                  apply changes to database
  -q                       operate in quiet mode

"""
from docopt import docopt

def default_handler(port, apply, q, number=None, timeout=None):
    print('port={0}, number={1}, timeout={2}, apply={3}, quiet={4}'.format(port, number, timeout, apply, q))

if __name__ == '__main__':
    docopt(__doc__, version='1.0.0rc2', handlers=globals())
