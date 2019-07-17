#!/usr/bin/env python3

def solution(n, coins):

	# Set up our array for trakcing results
	arr = [1] + [0] * n

	for coin in coins:
		for i in range(coin, n + 1):
			arr[i] += arr[i - coin]

	if n == 0:
		return 0
	else:
		return arr[n]

print('### Coin Denominations')
print('Target amount:\t100')
print('List of coins:\t[1, 2, 3]')
print('Solution:\t' + str(solution(100, [1, 2, 3])))