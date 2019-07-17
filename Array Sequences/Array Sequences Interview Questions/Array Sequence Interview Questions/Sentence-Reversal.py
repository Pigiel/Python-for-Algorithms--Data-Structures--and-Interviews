#!/usr/bin/env python3

""" Solution """
def rev_word1(s):
	return ' '.join(s.split()[::-1])
""" Practise """
def rev_word2(s):
	return ' '.join(reversed(s.split()))

def rev_word3(s):
	"""
	Manually doing the splits on the spaces.
	"""
	words = []
	length = len(s)
	spaces = [' ']

	# Index Tracker
	i = 0

	# While index is less than length of string
	while i < length:

		# If element isn't a space
		if s[i] not in spaces:

			# The word starts at this index
			word_start = i

			while i < length and s[i] not in spaces:
				# Get index where the word ends
				i += 1

			# Append that word to the list
			words.append(s[word_start:i])

		i += 1

	# Join the reversed words
	return ' '.join(reversed(words))

""" SOLUTION TESTING """
import unittest
class ReversalTest(unittest.TestCase):

	def test(self, sol):
		self.assertEqual(sol('    space before'),'before space')
		self.assertEqual(sol('space after     '),'after space')
		self.assertEqual(sol('   Hello John    how are you   '),'you are how John Hello')
		self.assertEqual(sol('1'),'1')
		print('ALL TEST CASES PASSED')

print("rev_word('Hi John,   are you ready to go?')")
print(rev_word1('Hi John,   are you ready to go?'))
print("rev_word('    space before')")
print(rev_word1('    space before'))

t = ReversalTest()
print('## Testing Solution 1')
t.test(rev_word1)
print('## Testing Solution 2')
t.test(rev_word2)
print('## Testing Solution 3')
t.test(rev_word3)