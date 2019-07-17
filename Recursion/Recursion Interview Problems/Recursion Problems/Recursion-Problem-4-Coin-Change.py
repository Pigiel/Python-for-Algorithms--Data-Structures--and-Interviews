#!/usr/bin/env python3

def rec_coin(target, coins):
	'''
	Args:
		Target change amount and list of coin values
	
	Returns:
		Minimum coins needed to make change

	Note: this solution is not optimized
	'''
	
	# Default to target value
	min_coins = target

	# CHeck to see if we have a single coint match (Base Case)
	if target in coins:
		return 1
	else:
		# For every coin value that is <= than target
		for i in [c for c in coins if c <= target]:
			# Recursive call (add a count coin and subtract from the target)
			num_coins = 1 + rec_coin(target - i, coins)

			# Reset minimum if we have a new minimum
			if num_coins < min_coins:
				min_coins = num_coins

	return min_coins

def rec_coin_dynam(target, coins, known_results):
	'''
	Args:
		This funciton takes in a target amount and a list of possible coins to use
		It also takes a third parameter, known_results, indicating previously calculated results
		
		The known_results parameter shoud be started with [0] * (target+1)
	
	Returns:
		Minimum number of coins needed to make the target

	'''

	# Default output to target
	min_coins = target

	# Base Case
	if target in coins:
		known_results[target] = 1
		return 1

	# Return a known result if it happens to be greater than 1
	elif known_results[target] > 0:
		return known_results[target]

	else:
		# For every coint value that is <= than target
		for i in [c for c in coins if c <= target]:

			# Recursive call, not how we include the known results!
			num_coins = 1 + rec_coin_dynam(target - i, coins, known_results)

			# Reset minimum if we have a new minimum
			if num_coins < min_coins:
				min_coins = num_coins

				# Reset the known result
				known_results[target] = min_coins

	return min_coins

print('rec_coin(10, [1,5]):\t' + str(rec_coin(10, [1,5])))
print('rec_coin(63,[1,5,10,25]):\t' + str(rec_coin(63,[1,5,10,25])))

target = 74
coins = [1,5,10,25]
known_results = [0]*(target + 1)

print('rec_coin_dynam({}, {}, {}):\t'.format(target, coins, known_results) + str(rec_coin_dynam(target, coins, known_results)))

""" SOLUTION TESTING """
import unittest

# NOTE: Non-dynamic functions will take a long time to test!
#		If you believe you have a solution
class TestCoins(unittest.TestCase):

	def test(self, solution):
		coins = [1, 5, 10, 25]
		self.assertEqual(solution(45, coins), 3)
		self.assertEqual(solution(23, coins), 5)
		self.assertEqual(solution(74, coins), 8)
		print('ALL TEST CASES PASSED')

# Run tests
t = TestCoins()
#t.test(rec_coin)