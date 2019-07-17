#!/usr/bin/env python3

def solution(unsorted_prices, max_price):

	# List of 0s at indices 0 to max_price
	prices_to_counts = [0] * (max_price+1)

	# Populate prices
	for price in unsorted_prices:
		prices_to_counts[price] += 1

	# Populate final sorted prices
	sorted_prices = []

	# For each price in prices_to_counts
	for price, count in enumerate(prices_to_counts):
		# For the number of times the element occurs
		for time in range(count):
			# Add it to the sorted price list
			sorted_prices.append(price)

	return sorted_prices

print('### Sorted prices')
print('List: [4,6,2,7,3,8,9]')
print('Max value: 9')
print(solution([4,6,2,7,3,8,9],9))