# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

n = int(input())
numbers = sorted(list(map(int, input().split())))

mean = sum(numbers) / n

if n % 2 != 0:
    median = numbers[n // 2]
else:
    index = n // 2
    median = (numbers[index] + numbers[index - 1]) / 2

occurrences = dict()
for n in set(numbers):
    if numbers.count(n) in occurrences:
        occurrences[numbers.count(n)].append(n)
    else:
        occurrences[numbers.count(n)] = [n]

mode = min(occurrences[max(occurrences.keys())])

print("{:.1f}\n{:.1f}\n{}".format(mean, median, mode))
