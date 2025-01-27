#!/usr/bin/env python3

def solution(lst):

	# Start at index 2 (3rd element) and assign highest and lowest
	# based off of the first two elements

	# Highest number so far
	high = max(lst[0], lst[1])

	# Lowest number so far
	low = min(lst[0], lst[1])

	# Initiate highest and lowest products of two numbers
	high_prod2 = lst[0] * lst[1]
	low_prod2 = lst[0] * lst[1]

	# Initiate highest product of 3 numbers
	high_prod3 = lst[0] * lst[1] * lst[2]

	# Iterate through list
	for num in lst[2:]:
		# Compare possible highest product of 3 numbers
		high_prod3 = max(high_prod3, num * high_prod2, num * low_prod2)

		# Check for possible new highest product of 2 numbers
		high_prod2 = max(high_prod2, num * high, num * low)

		# Check for possible new lowest product of 2 numbers
		low_prod2 = min(low_prod2, num * high, num * low)

		# Check for new possible high
		high = max(high, num)

		# Check for new possible low
		low = max(low, num)

	return high_prod3


print('### Highest product of 3 integers')
l = [99, -82, 82, 40, 75, -24, 39, -82, 5, 30, -25, -94, 93, -23, 48, 50, 49, -81, 41, 63]
print('List: ' + str(l))
print('Product: ' + str(solution(l)))