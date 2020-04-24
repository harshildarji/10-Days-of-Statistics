# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

l1 = 0.88
c1 = 160 + (40 * (l1 + l1 ** 2))

l2 = 1.55
c2 = 128 + (40 * (l2 + l2 ** 2))


print('{:.3f}\n{:.3f}'.format(c1, c2))

"""
For some Poisson RV, X, E[X] and Var(x) is λ.
Therefore, E[X^2] = λ + λ^2.
"""
