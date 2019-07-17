#!/usr/bin/env python3

def reverse(s):
	
	if len(s) <= 1:
		return s
	else:
		return reverse(s[1:]) + s[0]


print("reverse('hello world'):\t" + reverse('hello world'))

""" SOLUTION TESTING """
import unittest
class TestReverse(unittest.TestCase):

	def test(self, solution):
		self.assertEqual(solution('hello'),'olleh')
		self.assertEqual(solution('hello'),'olleh')
		self.assertEqual(solution('hello'),'olleh')
		print('ALL TEST CASES PASSED')

# Run tests
t = TestReverse()
t.test(reverse)