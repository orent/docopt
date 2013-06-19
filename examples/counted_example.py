"""Usage: counted_example.py --help
       counted_example.py -v...
       counted_example.py go [go]
       counted_example.py (--path=<path>)...
       counted_example.py <file> <file>

Try: counted_example.py -vvvvvvvvvv
     counted_example.py go go
     counted_example.py --path ./here --path ./there
     counted_example.py this.txt that.txt

"""
from docopt import docopt

def handle_v(v):
    print("v={0}".format(v))

def handle_go(go):
    print("go={0}".format(go))

def handle_path(path):
    for p in path:
        print("path={0}".format(p))

def handle_file(file):
    print("file1={0[0]}, file2={0[1]}".format(file))

docopt(__doc__, handlers=globals())
