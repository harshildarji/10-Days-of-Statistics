# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))


def get_std(l, mu):
    return (sum([(_l - mu) ** 2 for _l in l]) / n) ** 0.5


mu_x = sum(x) / n
std_x = get_std(x, mu_x)

mu_y = sum(y) / n
std_y = get_std(y, mu_y)

coef = sum([(_x - mu_x) * (_y - mu_y) for _x, _y in zip(x, y)]) / (n * std_x * std_y)
print("{:.3f}".format(coef))
