# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

from math import factorial as fact

l = 2.5
k = 5
e = 2.71828

print(round(((l ** k * e ** (-l)) / fact(k)), 3))
