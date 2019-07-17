#!/usr/bin/env python3

class Node:
	def __init__(self, value=None):
		self.left = None
		self.right = None
		self.value = value

# Python trick to pass infinity via string
INFINITY = float('infinity')
NEG_INFINITY = float('-infinity')

def isBST(tree, minVal=NEG_INFINITY, maxVal=INFINITY):
	
	if tree is None:
		return True
	
	if not minVal <= tree.value <= maxVal:
		return False

	return isBST(tree.left, minVal, tree.value) and isBST(tree.right, tree.value, maxVal)

# Using inorder tree traversal
def isBST2(tree, lastNode=[NEG_INFINITY]):

	if tree is None:
		return True

	if not isBST2(tree.left, lastNode):
		return False

	if tree.value < lastNode[0]:
		return False

	lastNode[0] = tree.value

	return isBST2(tree.right, lastNode)