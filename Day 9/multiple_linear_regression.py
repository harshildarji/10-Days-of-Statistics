# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

from sklearn import linear_model

m, n = list(map(int, input().split()))

X, Y = [], []
for _ in range(n):
    line = list(map(float, input().split()))
    X.append(line[:m])
    Y.append(line[-1])

q = int(input())

x_test = []
for _ in range(q):
    x_test.append(list(map(float, input().split())))

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

for x in x_test:
    print("{:.2f}".format(a + sum([(b[i] * x[i]) for i in range(m)])))
