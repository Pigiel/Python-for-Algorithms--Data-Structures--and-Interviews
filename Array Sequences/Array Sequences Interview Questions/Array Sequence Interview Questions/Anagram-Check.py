#!/usr/bim/env python3

""" Solution """
def anagram(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()
	return sorted(s1) == sorted(s2)

""" Practice """
def anagram2(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()

	# Edge Case Check
	if len(s1) != len(s2):
		return False

	count = {} # Create a hash table to count letters

	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1

	for letter in s2:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] = 1

	for k in count:
		if count[k] != 0:
			return False

	print('count: ' + str(count))
	return True
	
""" SOLUTION TESTING """
import unittest

class AnagramTest(unittest.TestCase):
	
	def test(self, sol):
		self.assertEqual(sol('go go go','gggooo'), True)
		self.assertEqual(sol('abc','cba'), True)
		self.assertEqual(sol('hi man','hi     man'), True)
		self.assertEqual(sol('aabbcc','aabbc'), False)
		self.assertEqual(sol('123','1 2'), False)
		print('ALL TEST CASES PASSED')


print('\n## SOLUTION')
print("anagram('dog','god')")
print(anagram('dog','god'))
print("anagram('clint eastwood','old west action')")
print(anagram('clint eastwood','old west action'))
print("anagram('aa','bb')")
print(anagram('aa','bb'))
# Run tests
print('## Test Cases')
t1 = AnagramTest()
t1.test(anagram)

print('\n## PRACTICE')
print('## Test Cases')
t2 = AnagramTest()
t2.test(anagram2)