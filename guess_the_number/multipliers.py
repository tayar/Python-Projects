import sys
import numpy as np

multiples = []

def multipliers_of_three_and_five(number):
	for x in range(number):
		if x%3 == 0:
			multiples.append(x)
		elif x%5 == 0:
			multiples.append(x)
	sum_of_multiples = np.sum(multiples)
	print sum_of_multiples
	
	
multipliers_of_three_and_five(1000)