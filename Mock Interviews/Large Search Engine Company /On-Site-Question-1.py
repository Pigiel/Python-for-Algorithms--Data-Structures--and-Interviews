#!/usr/bin/env python3
from random import randint

def dice7():
	return randint(1, 7)

def convert7to5():
	# Starting roll (just needs to be larger than 5)
	roll = 7

	while roll > 5:
		roll = dice7()
		print('dice7() produced a roll of ' + str(roll))
	
	return roll

print('Your final roll is ' + str(convert7to5()))