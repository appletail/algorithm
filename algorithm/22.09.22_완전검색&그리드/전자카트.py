import sys
sys.stdin = open("input.txt", "r")


def check(now, curS, cnt):
    global minV
    if curS > minV:
        return

    if cnt == N - 1:
        tmp = curS + ground[now][0]
        if tmp < minV:
            minV = tmp
        return

    for i in range(N):
        if ground[now][i] != 0 and not visited[i]:
            visited[i] = 1
            tmp = curS + ground[now][i]
            check(i, tmp, cnt + 1)
            visited[i] = 0



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] + [0] * (N - 1)
    minV = 1e10
    check(0, 0, 0)
    print(f'#{test_case}', minV)


# 다른 답
T = int(input())

INF = 1000


def dfs(start, status, cnt):
    global result

    if result <= status:
        return

    if cnt == N - 1:
        value = status + arr[start][0]

        if result > value:
            result = value

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(i, status + arr[start][i], cnt + 1)
                visited[i] = False


for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    visited[0] = True
    result = INF

    dfs(0, 0, 0)

    print(f'#{test_case} {result}')