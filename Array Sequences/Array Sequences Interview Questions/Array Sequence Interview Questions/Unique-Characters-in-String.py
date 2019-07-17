#!/usr/bin/env python3

""" Solution """
def uni_char1(s):
	return len(set(s)) == len(s)

def uni_char2(s):
	chars = set()
	for let in s:
		# Check if in set
		if let in chars:
			return False
		else:
			#Add it to the set
			chars.add(let)
	return True

""" Own """
def uni_char(s):
	characters = []
	for letter in s:
		if letter not in characters:
			characters += letter
		else:
			return False
	
	return True

""" SOLUTION TESTING """
import unittest
class TestUnique(unittest.TestCase):

	def test(self, sol):
		self.assertEqual(sol(''), True)
		self.assertEqual(sol('goo'), False)
		self.assertEqual(sol('abcdefg'), True)
		print('ALL TEST CASES PASSED')

t = TestUnique()
print('## Testing Own Solution')
t.test(uni_char)
print('## Testing Solution 1')
t.test(uni_char1)
print('## Testing Solution 2')
t.test(uni_char2)