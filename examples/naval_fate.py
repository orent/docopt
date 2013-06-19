"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -h | --help
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
import docopt

def handle_ship(**kw):
    def handle_new(name, **kw):
        for n in name:
            print('New ship {0}'.format(n))

    def handle_move(name, x, y, speed, **kw):
        print('Move ship {0} to ({1}, {2}) at speed {3}'.format(name[0], x, y, speed))

    def handle_shoot(x, y, **kw):
        print('Shoot at ({0}, {1})'.format(x, y))

    docopt.dispatch(kw, handlers=locals())

def handle_mine(**kw):
    def handle_set(x, y, moored=False, drifting=False, **kw):
        if moored:
            mode = 'moored '
        elif drifting:
            mode = 'drifting '
        else:
            mode = ''
        print('Set {0}mine at ({1}, {2})'.format(mode, x, y))

    def handle_remove(x, y, moored=False, drifting=False, **kw):
        if moored:
            mode = 'moored '
        elif drifting:
            mode = 'drifting '
        else:
            mode = ''
        print('Remove {0}mine at ({1}, {2})'.format(mode, x, y))

    docopt.dispatch(kw, handlers=locals())

if __name__ == '__main__':
    docopt.docopt(__doc__, version='Naval Fate 2.0', handlers=globals())
