#!/usr/bin/env python3
import collections

class Node:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

def levelOrderPrint(tree):
	
	if not tree:
		return

	nodes = collections.deque([tree])
	currentCount = 1
	nextCount = 0

	while len(nodes) != 0:
		
		currentNode = nodes.popleft()
		currentCount -= 1

		print(currentNode.value, end=' ')

		if currentNode.left:
			nodes.append(currentNode.left)
			nextCount += 1
		if currentNode.right:
			nodes.append(currentNode.right)
			nextCount += 1
		if currentCount == 0:
			# Finished printing current level
			print('\n')
			currentCount, nextCount = nextCount, currentCount

# Build a tree
#     1
#   2   3
# 4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

levelOrderPrint(root)