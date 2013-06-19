"""
usage: git remote [-v | --verbose]
       git remote add [-t <branch>] [-m <master>] [-f] [--mirror] <name> <url>
       git remote rename <old> <new>
       git remote rm <name>
       git remote set-head <name> (-a | -d | <branch>)
       git remote [-v | --verbose] show [-n] <name>
       git remote prune [-n | --dry-run] <name>
       git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
       git remote set-branches <name> [--add] <branch>...
       git remote set-url <name> <newurl> [<oldurl>]
       git remote set-url --add <name> <newurl>
       git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand

"""
import docopt

def handle_add(name, url, t, m, f, mirror, **kw):
    pass

def handle_rename(old, new, **kw):
    pass

def handle_rm(name, **kw):
    pass

def handle_set_head(name, a, d, branch, **kw):
    pass

def handle_show(name, verbose, n, **kw):
    pass

def handle_prune(name, dry_rune):
    pass

def handle_set_url(name, **kw):

    def handle_add(name, newurl, **kw):
        pass

    def handle_delete(name, url, **kw):
        pass

    def default_handler(name, newurl, oldurl, **kw):
        pass

#...

if __name__ == '__main__':
    docopt.docopt(__doc__, handlers=globals())
