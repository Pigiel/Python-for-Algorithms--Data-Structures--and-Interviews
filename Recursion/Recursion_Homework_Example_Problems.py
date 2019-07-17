#!/usr/bin/env python3

def rec_sum(n):
	# Base Case
	if n == 0:
		return 0
	# Recursion
	else:
		return n + rec_sum(n - 1)

def sum_func(n):
	# Base Case
	if n == 0:
		return 0
	# Recursion
	else:
		# Performing classing division in Python3 by using //
		return (n % 10) + sum_func(n // 10)

def word_split(phrase, list_of_words, output = None):
	'''
	NOTE: this is a very "python-y" solution
	'''
	
	# Checks to see if any output has been initiated
	# If you default output=[], it would be overwriteen every recursion!
	if output is None:
		output = []

	# For every word in list
	for word in list_of_words:
		# If the current phrase begins with the word, we have a split point!
		if phrase.startswith(word):
			# Add the word to the output
			output.append(word)
			# Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
			# Remember to pass along the output and list of words
			return word_split(phrase[len(word):], list_of_words, output)

	# Finally return output if no phrase.startswith(word) returns True
	return output

print('\n### Problem 1')
print('rec_sum(4):\t' + str(rec_sum(4)))
print('\n### Problem 2')
print('sum_func(4321):\t' + str(sum_func(4321)))
print('\n### Problem 3')
print("word_split('themanran',['the','ran','man']):")
print(str(word_split('themanran',['the','ran','man'])))
print("word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']):")
print(str(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])))
print("word_split('themanran',['clown','ran','man']):")
print(str(word_split('themanran',['clown','ran','man'])))