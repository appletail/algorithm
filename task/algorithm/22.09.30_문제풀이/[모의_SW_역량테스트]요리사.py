import sys
sys.stdin = open("input.txt", "r")


def mk_food(k, s):
    global minV

    if k == N // 2:
        sumA, sumB = 0, 0
        a, b = [], []
        for i in range(N):
            if visited[i]:
                a.append(i)
            else:
                b.append(i)

        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                sumA += synergy[a[i]][a[j]] + synergy[a[j]][a[i]]
                sumB += synergy[b[i]][b[j]] + synergy[b[j]][b[i]]

        minV = min(minV, abs(sumA - sumB))

    else:
        for i in range(s, N):
            if not visited[i]:
                visited[i] = 1
                mk_food(k + 1, i + 1)
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    minV = 1e10
    visited = [0] * N
    mk_food(0, 0)

    print(f'#{test_case}', minV)
