#! /usr/bin/env python

import random
from random import randint, sample, choice

stores = [i+1 for i in range(10)]
products = {(i+1):round(random.random()*100,2) for i in range(5)}

month = 9  # October
tran = "{store},{product},{quantity},{total_value},{time_of_transaction}\n"

def gendata():
	data = []
	for i in xrange(1,31): # from 1-Oct to 30-Oct
		number_of_customers = randint(1,100)
		for j in xrange(number_of_customers):
			_store = choice(stores)
			_products = [ products.keys()[k] for k in sorted(sample(xrange(len(products)), randint(1, len(products)))) ]	
			for p in _products:
				row = {}
				row['store'] = _store
				row['product'] = p
				row['quantity'] = randint(1,10)
				row['total_value'] = products[p]*row['quantity']
				row['time_of_transaction'] = "2016-{0}-{1}".format(month,i)
				# print tran.format(**row)
				data.append(tran.format(**row))
	return data

if __name__ == '__main__':
	datafile = open('data.txt','w')
	data = gendata()
	datafile.writelines(data)
	print "Wrote {} records.".format(len(data))
	datafile.close()