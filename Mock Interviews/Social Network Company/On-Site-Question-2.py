#!/usr/bin/env python3

def solution(id_list):

	# Initiate unique ID
	unique_id = 0

	# XOR for every ID in id list
	for i in id_list:
		print('Current ID:\t' + str(i))
		print('Unique ID:\t' + str(unique_id))
		print('XOR result:\t' + str((unique_id^i)))
		# XOR operation
		unique_id ^= i

	return unique_id

print('### Account ID')
print('\nList: [1,1,2,2,3]')
print('Account ID: ' + str(solution([1,1,2,2,3])))
print('\nList: [1,2,3,1,2,3]')
print('Account ID: ' + str(solution([1,2,3,1,2,3])))
print('\nList: [1,2,4,2,3,6,5]')
print('Account ID: ' + str(solution([1,2,4,2,3,6,5])))