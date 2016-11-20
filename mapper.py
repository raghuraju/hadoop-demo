#! /usr/bin/env python

import sys

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()

	data = line.split(',')

	print '{0}\t{1}'.format(data[0], data[3])