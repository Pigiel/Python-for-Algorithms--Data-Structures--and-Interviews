#!/usr/bin/env python3

def shell_sort(arr):
	
	sublistcount = len(arr) // 2

	# While we still have sub lists
	while sublistcount > 0:
		for start in range(sublistcount):
			# Use a gap insertion
			gap_insertion_sort(arr, start, sublistcount)

		sublistcount = sublistcount // 2

def gap_insertion_sort(arr, start, gap):
	for i in range(start + gap, len(arr), gap):

		currentValue = arr[i]
		position = i

		# Using the Gap
		while position >= gap and arr[position - gap] > currentValue:
			arr[position] = arr[position - gap]
			position = position - gap

		arr[position] = currentValue

print('\n### Shell Sort')
arr = [45, 67, 23, 45, 21, 24, 7, 2, 6, 4, 90]
print('List:\t' + str(arr))
shell_sort(arr)
print('Sorted:\t' + str(arr))