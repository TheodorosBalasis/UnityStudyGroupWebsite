import sys


def trim(s):
    try:
        return ' '.join(s.split())
    except:
        return s


def atoi(s):
    # convert object s to int without exception
    try:
        return int(s)
    except:
        return 0


def atob(s):
    # convert object s to bool without exception
    return bool(atoi(s))


def eprint(m):
    try:
        m = str(m)
    except:
        m = 'ERR: bad conversion'
    sys.stderr.write('\n%s\n\n' % (m,))
