import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    w, v = things[n]
    for k in range(1, K + 1):
        if w > k:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], v + dp[n - 1][k - w])

print(dp[N][K])
