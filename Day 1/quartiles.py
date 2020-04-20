# https://www.hackerrank.com/challenges/s10-quartiles/problem

n = int(input())
numbers = sorted(list(map(int, input().split())))

q2 = numbers[n//2] if n%2 != 0 else ((numbers[n//2] + numbers[n//2-1]) / 2)

lower = numbers[:n//2]
upper = numbers[n//2+1:] if n%2 != 0 else numbers[n//2:]

n_lower = len(lower)
n_upper = len(upper)

q1 = lower[n_lower//2] if n_lower%2 != 0 else ((lower[n_lower//2] + lower[n_lower//2-1]) / 2)
q3 = upper[n_upper//2] if n_upper%2 != 0 else ((upper[n_upper//2] + upper[n_upper//2-1]) / 2)

print('{:.0f}\n{:.0f}\n{:.0f}'.format(q1, q2, q3))
