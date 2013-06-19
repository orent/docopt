"""Example of program with many options using docopt.

Usage:
  options_example.py [-hvqrf NAME] [--exclude=PATTERNS]
                     [--select=ERRORS | --ignore=ERRORS] [--show-source]
                     [--statistics] [--count] [--benchmark] PATH...
  options_example.py (--doctest | --testsuite=DIR)
  options_example.py --version

Arguments:
  PATH  destination path

Options:
  -h --help            show this help message and exit
  --version            show version and exit
  -v --verbose         print status messages
  -q --quiet           report only file names
  -r --repeat          show all occurrences of the same error
  --exclude=PATTERNS   exclude files or directories which match these comma
                       separated patterns [default: .svn,CVS,.bzr,.hg,.git]
  -f NAME --file=NAME  when parsing directories, only check filenames matching
                       these comma separated patterns [default: *.py]
  --select=ERRORS      select errors and warnings (e.g. E,W6)
  --ignore=ERRORS      skip errors and warnings (e.g. E4,W)
  --show-source        show source code for each error
  --statistics         count errors and warnings
  --count              print total number of errors and warnings to standard
                       error and set exit code to 1 if total is not null
  --benchmark          measure processing speed
  --testsuite=DIR      run regression tests from dir
  --doctest            run doctest on myself

"""
from docopt import docopt

def handle_PATH(PATH, **kw):
    for k, v in kw.items():
        print('{0}={1}'.format(k, v))
    for p in PATH:
        print('path={0}'.format(p))

def handle_doctest(**kw):
    print('doctest')

def handle_testsuite(testsuite, **kw):
    print('testsuite={0}'.format(testsuite))

if __name__ == '__main__':
    docopt(__doc__, version='1.0.0rc2', handlers=globals())
