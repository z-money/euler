"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math, sys

def is_prime(n):
	"""
	Stolen from: https://en.wikipedia.org/wiki/Primality_test#Pseudocode
	"""
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i = i + 6
	return True

number = 600851475143
i = 1
highest_prime_factor = 1
while i*i <= number:
	if(number % i == 0):
		if(is_prime(number/i) and number/i > highest_prime_factor):
			highest_prime_factor = number/i
			break
		elif(is_prime(i) and i > highest_prime_factor):
			highest_prime_factor = i
	i += 1
print(highest_prime_factor)