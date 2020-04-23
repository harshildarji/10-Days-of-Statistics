# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

n, d = 1, 3
insp = 5

p = n / d
q = 1 - p

print(round((q**(insp-1) * p), 3))
