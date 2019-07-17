#!/usr/bin/env python3

class Queue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

print('Init a Queue:\tq = Queue()')
q = Queue()
print('Queue empty:\tq.isEmpty()')
print(q.isEmpty())
print('Inserting Int:\tq.enqueue(1)')
q.enqueue(1)
print('Inserting Str:\tq.enqueue("hi")')
q.enqueue('hi')
print('Inserting Bool:\tq.enqueue(True)')
q.enqueue(True)
print('Checking size:\tq.size()')
print(q.size())
print('Pop item:\tq.dequeue()')
print(q.dequeue())
print('Checking size:\tq.size()')
print(q.size())
print('Queue empty:\tq.isEmpty()')
print(q.isEmpty())