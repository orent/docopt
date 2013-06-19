"""Usage: odd_even_example.py [-h | --help] (ODD EVEN)...

Example, try:
  odd_even_example.py 1 2 3 4

Options:
  -h, --help

"""
from docopt import docopt

def default_handler(ODD, EVEN):
    for a, b in zip(ODD, EVEN):
        print('ODD={0}, EVEN={1}'.format(a, b))

if __name__ == '__main__':
    docopt(__doc__, handlers=globals())
