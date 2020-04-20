# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

n = int(input())
elements = input().split()
freq = list(map(int, input().split()))

numbers = []
for e, f in zip(elements, freq):
  numbers += list(map(int, [e] * f))

numbers = sorted(numbers)
n = len(numbers)

lower = numbers[:n//2]
upper = numbers[n//2+1:] if n%2 != 0 else numbers[n//2:]

n_lower = len(lower)
n_upper = len(upper)

q1 = lower[n_lower//2] if n_lower%2 != 0 else ((lower[n_lower//2] + lower[n_lower//2-1]) / 2)
q3 = upper[n_upper//2] if n_upper%2 != 0 else ((upper[n_upper//2] + upper[n_upper//2-1]) / 2)

print('{:.1f}'.format(q3-q1))
