#!/usr/bin/env python3

def bubble_sort(arr):
	# For every element (arranged backwards)
	for i in range(len(arr)-1, 0, -1):
		for k in range(i):
			if arr[k] > arr[k+1]:
				temp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = temp

print('\n### Bubble Sort')
arr = [ 3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
print('List:\t' + str(arr))
bubble_sort(arr)
print('Sorted:\t' + str(arr))