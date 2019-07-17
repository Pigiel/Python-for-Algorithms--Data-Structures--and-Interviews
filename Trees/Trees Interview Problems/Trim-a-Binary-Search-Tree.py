#!/usr/bin/env python3

class Node:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

def trimBST(tree, minVal, maxVal):

	if not tree:
		return

	tree.left = trimBST(tree.left, minVal, maxVal)
	tree.right = trimBST(tree.right, minVal, maxVal)

	if minVal <= tree.value <= maxVal:
		return tree

	if tree.value < minVal:
		return tree.right

	if tree.value > maxVal:
		return tree.left

### Checking the solution
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)

trimBST(root, 5, 13)