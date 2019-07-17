#!/usr/bin/env python3

def binary_search(arr, element):
	
	# First & last index value
	first = 0
	last = len(arr) - 1

	found = False

	while first <= last and not found:

		mid = (first + last) // 2 # // required for Python3 to get the floor

		# Match found
		if arr[mid] == element:
			found = True

		# set new midpoints up or down depending on comparison
		else:
			# Set down
			if element < arr[mid]:
				last = mid - 1
			# Set up
			else:
				first = mid + 1

	return found

print('\n### Binary Search algorythm')
# NOTE: List must be already sorted!
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('List:\t' + str(arr))
print('binary_search(arr, 4): ' + str(binary_search(arr, 4)))
print('binary_search(arr, 2.2): ' + str(binary_search(arr, 2.2)))