#!/usr/bin/env python3

def fib_rec(n):
	# Base Case
	if n == 0 or n == 1:
		return n
	# Recursion
	else:
		return fib_rec(n-1) + fib_rec(n-2)

# Instantiate Cache information
n = 23
cache = [None] * (n+1)

def fib_dyn(n):
	# Base Case
	if n == 0 or n == 1:
		return n
	
	# Check cashe
	if cache[n] != None:
		return cache[n]

	# Keep setting cache
	cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

	return cache[n]

def fib_iter(n):
	# Set starting point
	a = 0
	b = 1

	# Follow algorithm
	for i in range(n):
		a, b = b, a + b

	return a

""" SOLUTION TESTING """
import unittest

class TestFib(unittest.TestCase):

	def test(self, solution):
		self.assertEqual(solution(10),55)
		self.assertEqual(solution(1),1)
		self.assertEqual(solution(23),28657)
		print('ALL TEST CASES PASSED')

print('\n### Fibonnaci Sequence')
t = TestFib()
print('\n## Recursively')
print('fib_rec(10):\t' + str(fib_rec(10)))
t.test(fib_rec)
print('\n## Dynamically')
print('fib_dyn(10):\t' + str(fib_dyn(10)))
t.test(fib_dyn)
print('\n## Iteratively')
print('fib_iter(23):\t' + str(fib_iter(23)))
t.test(fib_iter)