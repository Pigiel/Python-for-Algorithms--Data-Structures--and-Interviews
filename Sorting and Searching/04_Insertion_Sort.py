#!/usr/bin/env python3

def insertion_sort(arr):
	# For every element in array
	for i in range(len(arr)-1, 0, -1):
		# Set current alues and position
		currentValue = arr[i]
		position = i

		# Sorted sublist
		while position > 0 and arr[position-1] > currentValue:
			arr[position] = arr[position-1]
			position = position-1

		arr[position] = currentValue

print('\n### Insertion Sort')
arr = [3, 5, 4, 6, 8, 1, 2, 12, 41, 25]
print('List:\t' + str(arr))
insertion_sort(arr)
print('Sorted:\t' + str(arr))