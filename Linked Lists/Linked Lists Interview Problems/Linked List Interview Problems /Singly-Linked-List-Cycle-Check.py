#!/usr/bin/env python3

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def cycle_check(node):
	
	# Begin both markers at the first node
	marker1 = node
	marker2 = node

	# Go until end of list
	while marker2 != None and marker2.nextnode != None:
		
		# Two runners - one faster than other
		marker1 = marker1.nextnode
		marker2 = marker2.nextnode.nextnode

		if marker2 == marker1:
			return True

	return False



""" SOLUTION TESTING """
import unittest

# Create cycle list
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!

# Create non cycle list
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

class TestCycleCheck(unittest.TestCase):

	def test(self, sol):
		self.assertEqual(sol(a),True)
		self.assertEqual(sol(x),False)
		print('ALL TEST CASES PASSED')

# Run tests
t = TestCycleCheck()
t.test(cycle_check)