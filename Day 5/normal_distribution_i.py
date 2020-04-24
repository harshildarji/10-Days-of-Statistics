# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

import math

mu, std = 20, 2
h1 = 19.5
min_h, max_h = 20, 22

e = 2.71828

def probability(x):
	return (1 + math.erf((x - mu) / (std * math.sqrt(2)))) / 2

print('{:.3f}\n{:.3f}'.format(probability(h1), probability(max_h) - probability(min_h)))
