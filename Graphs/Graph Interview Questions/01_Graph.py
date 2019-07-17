#!/usr/bin/env python3

from enum import Enum
from collections import OrderedDict

class State(Enum):
	unvisited = 1 # White
	visited = 2 # Black
	visiting = 3 # Grey

class Node:

	def __init__(self, key):
		self.key = key
		self.visit_state = State.unvisited
		self.adjacent = OrderedDict() # Key = node, Value = weight

	def __str__(self):
		return str(self.key)

class Graph:

	def __init__(self):
		self.nodes = OrderedDict() # Key = node id, Value = node

	def add_node(self, key):
		node = Node(key)
		self.nodes[key] = node
		return node

	def add_edge(self, source, destination, weight = 0):
		if source not in self.nodes:
			self.add_node(source)
		if destination not in self.nodes:
			self.add_node(destination)
		self.nodes[source].adjacent[self.nodes[destination]] = weight

print('### Graph implementation')
g = Graph()
print('\nAdding edge:\tg.add_edge(0, 1, 5)')
g.add_edge(0, 1, 5)
print(g.nodes)
print('\nAdding edge:\tg.add_edge(1, 2, 3)')
g.add_edge(1, 2, 3)
print(g.nodes)