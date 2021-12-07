#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
