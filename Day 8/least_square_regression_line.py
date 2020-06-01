# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

cov = var = 0
for i in range(len(x)):
    cov += (y[i] - y_mean) * (x[i] - x_mean)
    var += (x[i] - x_mean) ** 2

w1 = cov / var
w0 = y_mean - (w1 * x_mean)


def predict(x):
    return w0 + (w1 * x)


print("{:.3f}".format(predict(80)))
