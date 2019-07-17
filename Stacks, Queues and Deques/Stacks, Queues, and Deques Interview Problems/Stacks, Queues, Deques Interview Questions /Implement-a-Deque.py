#!/usr/bin/env python3

class Deque(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.insert(0, item)

	def addRear(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop(0)

	def removeRear(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

print('Init a Deque:\td = Deque()')
d = Deque()
print('Deque empty:\td.isEmpty()')
print(d.isEmpty())
print('Adding Front:\td.addFront(1)')
d.addFront(1)
print('Adding Rear:\td.addRear("there!")')
d.addRear('there!')
print('Adding Front:\td.addFront("Hi")')
d.addFront('Hi')
print('Checking size:\td.size()')
print(d.size())
print('Get items:\td.removeFront() + " " + d.removeRear()')
print(d.removeFront() + ' ' + d.removeRear())
print('Checking size:\td.size()')
print(d.size())
print('Deque empty:\td.isEmpty()')
print(d.isEmpty())