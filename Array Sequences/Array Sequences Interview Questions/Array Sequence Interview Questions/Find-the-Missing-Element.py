#!/usr/bin/env python3

""" Solution """
def finder1(arr1,arr2):
	
	# Sort the arrays
	arr1.sort()
	arr2.sort()

	# Compare elements in the sorted arrays
	for num1, num2 in zip(arr1, arr2):
		if num1 != num2:
			return num1

	# Otherwise return last element
	return arr1[-1]


import collections

def finder2(arr1, arr2):

	# Using default dict to avoid key errors
	d = collections.defaultdict(int)

	# Add a count for every instance in Array 1
	for num in arr2:
		d[num] += 1

	# Check in num not in dictionary
	for num in arr1:
		if d[num] == 0:
			return num

		# Otherwise, subtract a count
		else:
			d[num] -= 1

def finder3(arr1, arr2):
	result = 0

	# Perform an XOR between the numbers in the arrays
	for num in arr1 + arr2:
		result ^= num
		print(result)

	return result

""" Practice """
def finder4(arr1,arr2):
	num = 0
	for n in arr1:
		num += n
	for n in arr2:
		num -= n
	return num

""" Own """
def finder(arr1,arr2):
	for num in arr2:
		arr1.remove(num)
	return arr1[0]

""" SOLUTION TESTING """
import unittest
class TestFinder(unittest.TestCase):
	
	def test(self, sol):
		self.assertEqual(sol([5,5,7,7],[5,7,7]),5)
		self.assertEqual(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
		self.assertEqual(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
		print('ALL TEST CASES PASSED')

t = TestFinder()

print('\n## Arrays')
print('arr1 = [1,2,3,4,5,6,7]')
print('arr2 = [3,7,2,1,4,6]')
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]

print('\n## SOLUTION')
print('# Finder')
print(finder1(arr1,arr2))
t.test(finder1)
print('# Finder HASH')
print(finder2(arr1,arr2))
t.test(finder2)
print('# Finder XOR')
print(finder3(arr1,arr2))
t.test(finder3)
print('## PRACTICE')
print(finder4(arr1,arr2))
t.test(finder4)
print('## OWN')
print(finder(arr1,arr2))
t.test(finder)