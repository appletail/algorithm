import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()
dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[len(first)][len(second)])
