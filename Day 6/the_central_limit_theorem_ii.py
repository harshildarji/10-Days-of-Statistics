# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

import math

x, n, mu, sigma = 250, 100, 2.4, 2.0

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))
