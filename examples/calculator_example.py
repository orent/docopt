"""Not a serious example.

Usage:
  calculator_example.py <value> ( ( + | - | * | / ) <value> )...
  calculator_example.py <function> <value> [( , <value> )]...
  calculator_example.py (-h | --help)

Examples:
  calculator_example.py 1 + 2 + 3 + 4 + 5
  calculator_example.py 1 + 2 '*' 3 / 4 - 5    # note quotes around '*'
  calculator_example.py sum 10 , 20 , 30 , 40

Options:
  -h, --help

"""
from docopt import docopt

def apply(f, value):
    print('Result: {0}'.format(f(int(v) for v in value)))

def handle_function(function, value, **kw):
    f = getattr(__builtins__, function)
    apply(f, value)

def default_handler(value, **kw):
    op = ''.join(k for k, v in kw.items() if v)
    if len(op) > 1:
        print('Order of operators lost in parsing.')
        return

    import operator
    op_map = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    def f(x):
        return reduce(op_map[op], x)

    apply(f, value)

if __name__ == '__main__':
    docopt(__doc__, handlers=globals())
