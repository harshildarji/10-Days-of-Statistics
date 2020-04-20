# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

import math

n = int(input())
numbers = list(map(int, input().split()))

mean = sum(numbers)/n
squared_distances = [(num - mean)**2 for num in numbers]
std = math.sqrt(sum(squared_distances) / n)

print('{:.1f}'.format(std))
