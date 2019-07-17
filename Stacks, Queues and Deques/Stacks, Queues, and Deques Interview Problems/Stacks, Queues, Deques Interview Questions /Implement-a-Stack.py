#!/usr/bin/env python3

class Stack(object):

	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)


print('Init a Stack:\ts = Stack()')
s = Stack()
print('Stack empty:\ts.isEmpty()')
print(s.isEmpty())
print('Inserting Int:\ts.push(1)')
s.push(1)
print('Inserting Str:\ts.push("hi")')
s.push('hi')
print('Inserting Bool:\ts.push(True)')
s.push(True)
print('Checking size:\ts.size()')
print(s.size())
print('Checking peek:\ts.peek()')
print(s.peek())
print('Pop item:\ts.pop()')
print(s.pop())
print('Checking size:\ts.size()')
print(s.size())
print('Checking peek:\ts.peek()')
print(s.peek())
print('Stack empty:\ts.isEmpty()')
print(s.isEmpty())