#!/usr/bin/env python3

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None

def tree_max(node):
	if not node:
		return float('-inf')
	maxleft = tree_max(node.left)
	maxright = tree_max(node.right)
	return max(node.key, maxleft, maxright)

def tree_min(node):
	if not node:
		return float('inf')
	minleft = tree_min(node.left)
	minright = tree_min(node.right)
	return min(node.key, minleft, minright)

def verify(node):
	if not node:
		return True
	if (tree_max(node.left) <= node.key <= tree_min(node.right) and verify(node.left) and verify(node.right)):
		return True
	else:
		return False

# Check the solution
print('\n### Preferred solution')
root = Node(10, 'Hello')
root.left = Node(5, 'Five')
root.right = Node(30, 'Thirty')
print('# 1st Tree')
print(verify(root)) # prints True, since this tree is valid

root = Node(10, 'Ten')
root.right = Node(20, 'Twenty')
root.left = Node(5, 'Five')
root.left.right = Node(15, 'Fifteen')
print('# 2nd Tree')
print(verify(root)) # prints False, since 15 is to the left of 10

# Another valid solution using python trick
# Traversal the BST inorder will give you sorted values 
tree_vals = []

def inorder(tree):
	if tree != None:
		inorder(tree.left)
		tree_vals.append(tree.value)
		inorder(tree.right)

def sort_check(tree_vals):
	return tree_vals == sorted(tree_vals)

tree = Node(10, 'Hello')
tree.left = Node(5, 'Five')
tree.right= Node(30, 'Thirty')
print('\n### In order traversal')
print('# 1st Tree')
inorder(tree)
print(sort_check(tree_vals))

tree = Node(10, 'Ten')
tree.right = Node(20, 'Twenty')
tree.left = Node(5, 'Five')
tree.left.right = Node(15, 'Fifteen')
print('# 2nd Tree')
inorder(tree)
print(sort_check(tree_vals))