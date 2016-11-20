#!/usr/bin/env python

from operator import itemgetter
import sys

current_store = None
current_revenue = 0
store = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    store, revenue = line.split('\t', 1)

    # convert revenue into float
    try:
        revenue = float(revenue)
    except ValueError:
        # revenue is not a float, so silently
        # ignore/discard this line
        continue

    if not current_store:
        current_store = store

    if current_store == store:
        current_revenue += revenue
    else:
        if current_store:
            # write result to STDOUT
            print '%s\t%s' % (current_store, current_revenue)
        current_store = store
        current_revenue = revenue

print("\t".join(str(v) for v in [current_store, current_revenue]))
