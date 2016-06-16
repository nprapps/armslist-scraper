from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    """Prints to standard error instead of standard out"""
    print(*args, file=sys.stderr, **kwargs)
