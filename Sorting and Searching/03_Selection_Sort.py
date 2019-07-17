#!/usr/bin/env python3

def selection_sort(arr):
	# For every element in array
	for i in range(len(arr)-1, 0, -1):
		positionOfMax = 0

		for location in range(1, i+1):
			# Set maximum's location
			if arr[location] > arr[positionOfMax]:
				positionOfMax = location

		temp = arr[i]
		arr[i] = arr[positionOfMax]
		arr[positionOfMax] = temp

print('\n### Selection Sort')
arr = [3, 5, 2, 7, 6, 8, 12, 40, 21]
print('List:\t' + str(arr))
selection_sort(arr)
print('Sorted:\t' + str(arr))