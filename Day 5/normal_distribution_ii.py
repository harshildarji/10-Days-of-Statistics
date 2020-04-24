# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math

mu, std = 70, 10

s1 = 80
s2 = 60

def probability(x):
	return ((1 + math.erf((x - mu) / (std * math.sqrt(2)))) / 2) * 100

higher = 100 - probability(80)
passed = 100 - probability(60)
failed = probability(60)

print('{:.2f}\n{:.2f}\n{:.2f}'.format(higher, passed, failed))
