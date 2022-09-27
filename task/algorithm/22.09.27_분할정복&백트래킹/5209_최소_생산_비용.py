import sys
sys.stdin = open("input.txt", "r")


def minCost(k, curS):
    global result

    if curS >= result:
        return

    if k == N:
        result = min(result, curS)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                minCost(k + 1, curS + factories[k][i])
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 99 * N
    minCost(0, 0)
    print(f'#{test_case} {result}')