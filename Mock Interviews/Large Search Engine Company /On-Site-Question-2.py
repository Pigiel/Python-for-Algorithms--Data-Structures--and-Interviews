#!/usr/bin/env python3
from random import randint

def dice5():
	return randint(1, 5)

def convert5to7():
	# For constant re-roll purposes
	while True:
		# Roll the dice twice
		roll_1 = dice5()
		roll_2 = dice5()

		print('The rolls were {} & {}'.format(roll_1, roll_2))

		# Convert the combination to the range 1 to 25
		num = (roll_1 - 1) * 5 + roll_2

		print('The converted range was: ' + str(num))

		if num > 21:
			# Re-roll if we are out of range
			continue

		return num % 7 + 1

print('Your final roll is ' + str(convert5to7()))