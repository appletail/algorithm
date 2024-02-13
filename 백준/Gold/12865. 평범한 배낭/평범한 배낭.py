N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w - 1, -1):
        if dp[i] < (tmp := dp[i - w] + v):
            dp[i] = tmp

print(dp[K])