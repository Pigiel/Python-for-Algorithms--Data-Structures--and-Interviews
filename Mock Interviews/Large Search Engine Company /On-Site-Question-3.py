#!/usr/bin/env python3

def reverse(s):
	# Base case
	if len(s) <= 1:
		return s
	# Recursion
	return reverse(s[1:]) + s[0]
		

print(reverse('hello world'))