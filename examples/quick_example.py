"""Usage:
  quick_example.py tcp <host> <port> [--timeout=<seconds>]
  quick_example.py serial <port> [--baud=9600] [--timeout=<seconds>]
  quick_example.py -h | --help | --version

"""
from docopt import docopt

def handle_tcp(host, port, timeout=None):
    print('host={0} port={1} timeout={2}'.format(host, port, timeout))

def handle_serial(port, baud=None, timeout=None):
    print('port={0} baud={1} timeout={2}'.format(port, baud, timeout))

if __name__ == '__main__':
    docopt(__doc__, version='0.1.1rc', handlers=globals())
