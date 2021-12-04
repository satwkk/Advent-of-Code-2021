#!/usr/bin/env python3

gamma_rate = ''
epsilon_rate = ''
power_consumption = 0

''' Parsing input file'''
with open('input-part1.txt', 'r') as f:
    binary_nums = f.readlines()

binary_nums = [binary_nums[i].strip() for i in range(len(binary_nums))]

def convert_binary_to_int(num):
	return int(num, 2)

def find_rates(index, search=None):
	digits = []
	result = ""
	for num in binary_nums:
		digits.append(num[index])

	if search == 'gamma':
		if digits.count('1') > digits.count('0'):
			result += '1'
		else:
			result += '0'
	if search == 'epsilon':
		if digits.count('1') < digits.count('0'):
			result += '1'
		else:
			result += '0'
   
	return result

for i in range(len(binary_nums[0])):
	gamma = find_rates(i, 'gamma')
	epsilon = find_rates(i, 'epsilon')
	# epsilon = find_epsilon_rate(i)

	gamma_rate += gamma
	epsilon_rate += epsilon

gamma_decimal = convert_binary_to_int(gamma_rate)
epsilon_decimal = convert_binary_to_int(epsilon_rate)
power_consumption = gamma_decimal * epsilon_decimal
print(f'Part1: {power_consumption}')

# Part 2
