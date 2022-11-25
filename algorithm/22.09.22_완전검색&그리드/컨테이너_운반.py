import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    sumV = 0
    used = []

    for i in range(m):
        curC, curI = 0, -1
        for j in range(n):
            if t[i] >= w[j] >= curC and j not in used:
                curC, curI = w[j], j
        sumV += curC
        if curI > -1:
            used.append(curI)

    print(f'#{test_case}', sumV)