# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

import math

n, mu, sigma, percent, z = 100, 500, 80, 0.95, 1.96

sample_std = sigma / (math.sqrt(n))
A = mu - (z * sample_std)
B = mu + (z * sample_std)
print("{:.2f}\n{:.2f}".format(A, B))
