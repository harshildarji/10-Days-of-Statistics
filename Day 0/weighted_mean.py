# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

n = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

weighted_mean = sum(a[0] * a[1] for a in zip(arr_1, arr_2)) / sum(arr_2)
print("{:.1f}".format(weighted_mean))
