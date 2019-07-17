#!/usr/bin/env python3

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def reverse(head):

	# Set up current, previous and next nodes
	current = head
	previous = None
	nextnode = None

	# Until we have gone through to the end of the list
	while current:
		# Make sure to copy the current nodes next node to a variable next_node
		# Before overwriting as the previous node for reversal
		nextnode = current.nextnode

		# Reverse the pointer to the next node
		current.nextnode = previous

		# Go one forward in the list
		previous = current
		current = nextnode

	return previous

""" SOLUTION TESTING """
import unittest

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with value 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
try:
	print(d.nextnode.value)
except Exception as e:
	print(e)

reverse(a) # Reverse the linked list

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
try:
	print(a.nextnode.value)
except Exception as e:
	print(e)