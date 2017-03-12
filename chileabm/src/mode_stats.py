""" 
simple mode stats calculation

Arika Ligmann-Zielinska

Feb 03, 2016
"""
import random

def mode(datalist):
	"""calculate mode value of input list of str
	procedure:
		[1] create a collection of unique values from input list
		[2] for each value in this collection, count the number
			of occurences of that value in input list
		[3] build a list of tuples (count, value)  - DICTIONARY would be OK but {value: count}
		[4] return max from list [3]
	"""
	# [1] we could use a for loop but there is a shorter version:
	uniquelist = set(datalist)
	# [2] iterate over the unique values and count their occurence in input list
	counts = []
	for val in uniquelist:
		counts.append(datalist.count(val))
	# [3] build a list of tuples
	vat = zip(counts,uniquelist)
	# [4] sort the vat from max to min count
	vat = sorted(vat, reverse=True)
	# [5] get all modal values
	vat = [val for val in vat if val[0] == max(counts)]
	randmode = random.choice(vat) 
	return randmode[1] # just the str, not count



# testing
if __name__ == "__main__":
	colors = ['red','green','red', 'green', 'blue','yellow','blue']
	print "list of colors\t",colors
	amode = mode(colors)
	print "selected mode:",amode
