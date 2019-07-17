#!/usr/bin/env python3

def remove_duplicates(string):
	
	results = []
	seen = set()

	for char in string:
		if char not in seen:
			seen.add(char)
			results.append(char)
	
	return ''.join(results)

print('### Remove duplicates')
print('tree traversal:\t' + remove_duplicates('tree traversal'))