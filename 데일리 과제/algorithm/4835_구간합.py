import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))

    maxv = 0
    minv = 9999999999
    for j in range(N - M + 1):
        sumv = 0
        for k in range(M):
            sumv += num_lst[j + k]
        if sumv > maxv:
            maxv = sumv
        if sumv < minv:
            minv = sumv

    print(f'#{i + 1} {maxv - minv}')
