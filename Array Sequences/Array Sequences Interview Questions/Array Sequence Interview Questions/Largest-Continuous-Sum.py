#!/usr/bin/env python3

""" Solution """
def large_cont_sum(arr): 
	
	# Check to see if array is length 0
	if len(arr) == 0:
		return 0

	# Start the max and current sum at the first element
	max_sum = current_sum = arr[0]

	# For every element in array
	for num in arr[1:]:
		# Set current sum as the higher of the two
		current_sum = max(current_sum + num, num)
		# Set max as the higher between the currentSum and the current max
		max_sum = max(current_sum, max_sum)

	return max_sum

""" SOLUTION TESTING """
import unittest
class LargeContTest(unittest.TestCase):
	
	def test(self, sol):
		self.assertEqual(sol([1,2,-1,3,4,-1]),9)
		self.assertEqual(sol([1,2,-1,3,4,10,10,-10,-1]),29)
		self.assertEqual(sol([-1,1]),1)
		print('ALL TEST CASES PASSED')

print('\n## SOLUTION')
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

t = LargeContTest()
t.test(large_cont_sum)