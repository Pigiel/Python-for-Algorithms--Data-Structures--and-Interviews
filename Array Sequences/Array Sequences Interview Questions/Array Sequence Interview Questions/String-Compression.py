#!/usr/bin/env python3

""" Solution """
def compress1(s):
	"""
	This solution compresses without chacking. Known as the RunLength Compression algorithm.
	"""

	# Begin Run as empty string
	r = ''
	l = len(s)

	# Check for length 0
	if l == 0:
		return ''

	# Check for length 1
	if l == 1:
		return s + '1'

	# Initialize values
	last = s[0]
	cnt = 1
	i = 1

	while i < l:

		# Check to see if it is the same letter
		if s[i] == s[i - 1]:
			# Add a count if same as previous
			cnt += 1
		else:
			# Otherwise store the previous data
			r = r + s[i - 1] + str(cnt)
			cnt = 1

		# Add to index count to terminate while loop
		i += 1

	# Put everyghing back into run
	r = r + s[i - 1] + str(cnt)

	return r

""" Own """
import collections

def compress(s):

	d = collections.OrderedDict()
	compressed = ''

	for letter in s:
		if letter not in d:
			d[letter] = 1
		else:
			d[letter] += 1

	for letter, count in d.items():
		compressed += letter + str(count)

	return compressed

""" SOLUTION TESTING """
import unittest
class TestCompress(unittest.TestCase):

	def test(self, sol):
		self.assertEqual(sol(''), '')
		self.assertEqual(sol('AABBCC'), 'A2B2C2')
		self.assertEqual(sol('AAABCCDDDDD'), 'A3B1C2D5')
		print('ALL TEST CASES PASSED')


print('AAAAABBBBCCCC')
print(compress('AAAAABBBBCCCC'))

t = TestCompress()
print('## Testing Solution')
t.test(compress1)
print('## Testing Own Solution')
t.test(compress)