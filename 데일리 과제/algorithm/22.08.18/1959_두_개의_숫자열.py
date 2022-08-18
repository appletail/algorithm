import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        ai, bj = bj, ai

    maxV = 0

    for i in range(m - n + 1):
        sumV = 0
        for j in range(n):
            sumV += ai[j] * bj[i + j]
        if maxV < sumV:
            maxV = sumV

    print(f'#{test_case} {maxV}')