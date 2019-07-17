#!/usr/bin/env python3

def profit(stock_prices):

	# Start minimum prices marker at first price
	min_stock_price = stock_prices[0]

	# Start off with a profit of zero
	max_profit = 0

	for price in stock_prices:
		# Check to set the lowest stock price so far
		min_stock_price = min(min_stock_price, price)

		# Check the current price against our minimum for a profit
		# comparison against the max_profit
		comparison_profit = price - min_stock_price

		# Compare against our max_profit so far
		max_profit = max(max_profit, comparison_profit)

	return max_profit

def profit2(stock_prices):
	# Check length
	if len(stock_prices) < 2:
		#raise Exception('Need at least two stock prices!')
		return 'Exception: Need at least two stock prices!'

	# Start minimum price marker at first price
	min_stock_price = stock_prices[0]

	# Start off with an initial max profit
	max_profit = stock_prices[1] - stock_prices[0]

	# Skip first index of 0
	for price in stock_prices[1:]:
		# NOTE THE REORDERING HERE DUE TO THE NEGATIVE PROFIT TRACKING
		
		# Check the current price against our minimum for a profit
		# comparison against the max_profit
		comparison_profit = price - min_stock_price

		# Compare against our max_profit so far
		max_profit = max(max_profit, comparison_profit)

		# Check to set the lowest stock price so far
		min_stock_price = min(min_stock_price, price)

	return max_profit

print('### Stock Prices')
print('\n# Greedy algorytm')
print('Stock: [10,12,14,12,13,11,8,7,6,13,23,45,11,10]')
print(profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10]))
print('\n# Improved for edge cases ')
print('\nException for less than 2 stock prices in list')
print('Stock: [1]')
print(profit2([1]))
print('\nPrices goes down - negative profit')
print('Stock: [30,22,21,5]')
print(profit2([30,22,21,5]))