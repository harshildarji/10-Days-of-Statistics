# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

n, d = 1, 3
insp = 5

p = n / d
q = 1 - p

print(round(sum([q**(i-1) * p for i in range(1, 6)]), 3))
