#!/usr/bin/env python3

class LinkedListNode(object):
	
	def __init__(self, value):
		self.value = value
		self.nextnode = None

class DoublyLinkedListNode(object):
	
	def __init__(self, value):
		self.value = value
		self.next_node = None
		self.prev_node = None

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.nextnode = b
b.nextnode = c

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

# Setting b after a
a.next_node = b
b.prev_node = a
# Setting c after b
b.next_node = c
c.prev_node = b