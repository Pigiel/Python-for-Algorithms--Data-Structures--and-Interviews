#!/usr/bin/env python3

class Queue2Stacks(object):

	def __init__(self):

		# Two Stacks
		self.instack = []
		self.outstack = []

	def enqueue(self, element):
		# Add an enqueue with the "IN" stack
		self.instack.append(element)

	def dequeue(self):
		if not self.outstack:
			while self.instack:
				# Add the elements to the outstack to reverse the order when called
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()

""" SOLUTION TESTING """
q = Queue2Stacks()

for i in range(5):
	q.enqueue(i)

for i in range(5):
	print(q.dequeue())