"""Usage: arguments_example.py [-vqrh] [FILE] ...
          arguments_example.py (--left | --right) CORRECTION FILE

Process FILE and optionally apply correction to either left-hand side or
right-hand side.

Arguments:
  FILE        optional input file
  CORRECTION  correction angle, needs FILE, --left or --right to be present

Options:
  -h --help
  -v       verbose mode
  -q       quiet mode
  -r       make report
  --left   use left-hand side
  --right  use right-hand side

"""
from docopt import docopt

def process_files(angle, files, v=False, q=False, r=False):
    for file in files:
        print('file={0}, angle={1}'.format(file, angle))
    print('verbose={0}, quiet={1}, report={2}'.format(v, q, r))

def handle_right(CORRECTION, FILE, **opts):
    process_files(int(CORRECTION), FILE, **opts)

def handle_left(CORRECTION, FILE, **opts):
    process_files(-int(CORRECTION), FILE, **opts)

def default_handler(FILE, **opts):
    process_files(0, FILE, **opts)

if __name__ == '__main__':
    docopt(__doc__, handlers=globals())
