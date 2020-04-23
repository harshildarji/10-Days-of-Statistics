# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

from math import factorial as fact

b, g = 1.09, 1

p = b / (b + 1)
q = 1 - p

n = 6

def get_bin_dist(x):
    return ((fact(n) / ((fact(x)) * (fact(n-x))) * (p**x) * (q**(n-x))))

proportion = round(sum(get_bin_dist(x) for x in range(3, 7)), 3)
print(proportion)