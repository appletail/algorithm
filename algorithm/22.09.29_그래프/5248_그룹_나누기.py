import sys
sys.stdin = open("input.txt", "r")


def dfs(k):
    s = [k]
    while s:
        v = s.pop()
        visited[v] = 1
        for w in nodes[v]:
            if not visited[w]:
                s.append(w)


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    nodes = [[] for _ in range(n + 1)]
    tmp = list(map(int, input().split()))
    for i in range(0, m * 2, 2):
        nodes[tmp[i]].append(tmp[i + 1])
        nodes[tmp[i + 1]].append(tmp[i])

    visited = [0] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            cnt += 1
            dfs(i)

    print(f'#{test_case}', cnt)
