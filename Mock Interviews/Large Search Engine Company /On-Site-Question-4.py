#!/usr/bin/env python3

def solution(num):
	if num < 0:
		print('ValueError - provide positive number')
		#raise ValueError
	if num == 1:
		return 1

	for k in range((num//2) + 1):
		if k**2 == num:
			return k
		elif k**2 > num:
			return k - 1

	return k

# Better solution using binary search
def solution_binary(num):
	if num < 0:
		print('ValueError - provide positive number')
		#raise ValueError
	if num == 1:
		return 1

	low = 0
	high = (num // 2) + 1

	while low + 1 < high:
		mid = low + (high - low) // 2
		square = mid**2
		if square == num:
			return mid
		elif square < num:
			low = mid
		else:
			high = mid

	return low

print('### Squareroot of number rounded down')
print('\n# Linear algorythm')
print('solution(14): ' + str(solution(14)))
print('solution(15): ' + str(solution(15)))
print('solution(16): ' + str(solution(16)))
print('\n# Binary search algorythm')
print('solution_binary(14): ' + str(solution_binary(14)))
print('solution_binary(15): ' + str(solution_binary(15)))
print('solution_binary(16): ' + str(solution_binary(16)))