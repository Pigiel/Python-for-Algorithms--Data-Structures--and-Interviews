#!/usr/bin/env python3

def solution(lst, target):

	# Create set to keep track of duplicates
	seen = set()

	# We want to find if there is a num2 that sums with num to reach the target
	for num in lst:
		
		num2 = target - num
		
		if num2 in seen:
			return True
		
		seen.add(num)

	# If we never find a pair match which ceates the sum
	return False

print('### Sum of two integers')
print('\nList: [1,3,5,1,7]')
print('Sum: 4')
print(solution([1,3,5,1,7], 4))
print('\nList: [1,3,5,1,7]')
print('Sum: 14')
print(solution([1,3,5,1,7], 14))