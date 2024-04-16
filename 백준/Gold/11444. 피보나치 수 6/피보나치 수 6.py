def fibo(n):
    if dp.get(n):
        return dp[n]
    else:
        half = n // 2
        if n % 2:
            dp[n] = (fibo(half)**2 + fibo(half+1)**2) % 1_000_000_007
            return dp[n]
        else:
            dp[n] = (fibo(half) * (2*fibo(half-1) + fibo(half))) % 1_000_000_007
            return dp[n]

num = int(input())
dp = {1: 1, 2: 1}

print(fibo(num))
