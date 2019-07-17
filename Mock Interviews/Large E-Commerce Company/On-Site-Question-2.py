#!/usr/bin/env python3

def index_prod(lst):

	# Create an empty output list
	output = [None] * len(lst)

	# Set initial product and index for Greedy run Forward
	product = 1
	i = 0

	while i < len(lst):
		# Set index as cumulative product
		output[i] = product
		# Cumulative product
		product *= lst[i]
		# Move forward
		i += 1

	# Now for our Greedy run Backwards
	product = 1
	# Start index at last (taking into account index 0)
	i = len(lst) - 1

	# Until the beginning of the list
	while i >= 0:
		# Same operations as before, just backwards
		output[i] *= product
		product *= lst[i]
		i -= 1

	return output

print('### Inex production')
print('List: [1,2,3,4]')
print(index_prod([1,2,3,4]))
print('List: [0,1,2,3,4]')
print(index_prod([0,1,2,3,4]))