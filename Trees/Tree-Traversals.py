#!/usr/bin/env python3

class BinaryTree(object):

	# Init the root of a tree with key set to root variable
	def __init__(self, root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		# If there is no left child insert new one
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		# If there is then move it down one level and insert new child
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		# If there is no right child insert new one
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		# If there is then move it down one level and insert new child
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def setRootValue(self, newRoot):
		self.key = newRoot

	def getRootValue(self):
		return self.key

def preorder(tree):
	if tree != None:
		print(tree.getRootValue())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print(tree.getRootValue())
		inorder(tree.getRightChild())

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootValue())

# Create a Binary tree
#       1
#     2   3
#   4       5
t = BinaryTree(1)
t.insertLeft(4)
t.insertLeft(2)
t.insertRight(5)
t.insertRight(3)

# Tree traversals
print('### Preorder')
preorder(t)
print('### Inorder')
inorder(t)
print('### Postorder')
postorder(t)