#!/usr/bin/env python3

def permute(s):
	out = []

	# Base Case
	if len(s) == 1:
		out = [s]
	else:
		# For every letter in string
		for i, let in enumerate(s):
			# For every permutation resulting from Step 2 and 3 described above
			for perm in permute(s[:i] + s[i+1:]):
				out += [let + perm]
	return out

print("permute('abc'):\t" + str(permute('abc')))

""" SOLUTION TESTING """
import unittest

class TestPerm(unittest.TestCase):

	def test(self, solution):
		self.assertEqual(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
		self.assertEqual(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))
		print('ALL TEST CASES PASSED')

t = TestPerm()
t.test(permute)