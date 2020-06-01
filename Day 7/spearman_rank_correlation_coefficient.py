# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))


def get_rank(l):
    set_l = list(sorted(set(l)))
    return [set_l.index(_l) + 1 for _l in l]


rx = get_rank(x)
ry = get_rank(y)

r = 1 - ((6 * sum([(_x - _y) ** 2 for _x, _y in zip(rx, ry)])) / (n * (n ** 2 - 1)))
print("{:.3f}".format(r))
