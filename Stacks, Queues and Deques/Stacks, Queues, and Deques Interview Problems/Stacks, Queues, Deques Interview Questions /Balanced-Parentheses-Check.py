#!/usr/bin/env python3

def balance_check(s):
	
	# Check if even number of brackets
	if len(s) % 2 != 0:
		return False

	# Set of opening brackets
	opening = set('([{')

	# Matching pairs
	matches = set([('(',')'), ('[',']'), ('{','}')])

	# Use a list as a "Stack"
	stack = []

	# Check every parenthesis in string
	for paren in s:

		# If its an opening, append it to list
		if paren in opening:
			stack.append(paren)

		else:
			# Check that there are parentheses in Stack
			if len(stack) == 0:
				return False

			# Check the last open parentheses
			last_open = stack.pop()

			# Check if it has a closing match
			if (last_open, paren) not in matches:
				return False

	return len(stack) == 0

balance_check('[]')
balance_check('[](){([[[]]])}')
balance_check('()(){]}')

""" SOLUTION TESTING """
import unittest
class TestBalanceCheck(unittest.TestCase):

	def test(self, sol):
		self.assertEqual(sol('[](){([[[]]])}('),False)
		self.assertEqual(sol('[{{{(())}}}]((()))'),True)
		self.assertEqual(sol('[[[]])]'),False)
		print('ALL TEST CASES PASSED')

t = TestBalanceCheck()
t.test(balance_check)