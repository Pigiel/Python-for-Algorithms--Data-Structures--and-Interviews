#!/usr/bin/env python3

""" Solution """
def pair_sum(arr,k):
	
	if len(arr) < 2:
		return

	# Sets for tracking
	seen = set()
	output = set()

	# For every number in array
	for num in arr:
		# Set target difference
		target = k - num
		# Add it to set if target hasn't been seen
		if target not in seen:
			seen.add(num)
		else:
			# Add a tuple with the corresponding pair
			output.add( (min(num, target), max(num, target)) )

	# For testing
	print('seen:\t' + str(seen))
	print('output:\t' + str(output))
	return len(output)

""" Practice """
def pair_sum2(arr,k):
	
	counter = 0
	lookup = set()
	
	for num in arr:
		if k-num in lookup:
			counter += 1
		else:
			lookup.add(num)
	
	print('counter: ' + str(counter))
	print('lookup:\t' + str(lookup))
	return counter

""" SOLUTION TESTING """
import unittest
class TestPair(unittest.TestCase):
	
	def test(self,sol):
		self.assertEqual(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
		self.assertEqual(sol([1,2,3,1],3),1)
		self.assertEqual(sol([1,3,2,2],4),2)
		print('ALL TEST CASES PASSED')

t = TestPair()

print('\n## SOLUTION')
print('pair_sum([1,3,2,2],4)')
print(pair_sum([1,3,2,2],4))
print('## Test Cases')
t.test(pair_sum)

print('\n## PRACTICE')
print('pair_sum_practice([1,3,2,2],4)')
print(pair_sum2([1,3,2,2],4))
print('## Test Cases')
t.test(pair_sum2)