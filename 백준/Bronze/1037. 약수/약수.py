import sys
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))

n_lst.sort()

minimum = n_lst[0]
maximum = n_lst[-1]

print(minimum * maximum)
