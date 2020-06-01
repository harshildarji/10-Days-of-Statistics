# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

from math import factorial as fact

b, g = 12, 10

p = 0.12
q = 1 - p

n = 10


def get_bin_dist(x):
    return fact(n) / ((fact(x)) * (fact(n - x))) * (p ** x) * (q ** (n - x))


at_most = round(sum(get_bin_dist(x) for x in range(0, 3)), 3)
at_least = round(sum(get_bin_dist(x) for x in range(2, 11)), 3)
print("{}\n{}".format(at_most, at_least))
