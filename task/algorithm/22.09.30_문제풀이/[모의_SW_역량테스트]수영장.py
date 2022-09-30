import sys
sys.stdin = open("input.txt", "r")


def swim(k, cost):
    global minV
    if cost == minV:
        return

    if k >= 12:
        minV = min(minV, cost)
    else:
        # day
        swim(k + 1, cost + m_plan[k] * d)
        # month
        swim(k + 1, cost + m)
        # three month
        if k <= 9:
            swim(k + 3, cost + tm)


T = int(input())
for test_case in range(1, T + 1):
    d, m, tm, y = map(int, input().split())
    m_plan = list(map(int, input().split()))
    minV = y
    swim(0, 0)
    print(f'#{test_case}', minV)


# 다른 답
t = int(input())
for tc in range(1, t + 1):
    cost = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        tmp = [0, 0, cost[2] * 4, cost[3]]
        tmp[0] = dp[i - 1] + plan[i] * cost[0]
        tmp[1] = dp[i - 1] + cost[1]
        if i >= 2:
            tmp[2] = dp[i - 3] + cost[2]
        dp[i] = min(tmp)

    print(f'#{tc} {dp[12]}')