import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for j in range(N):
    for i in range(0, j+1):
        S, E = i, j
        if nums[i] != nums[j]:
            continue
        S += 1
        E -= 1
        if S > E or dp[S][E]:
            dp[i][j] = 1

for S, E in questions:
    print(dp[S-1][E-1])
