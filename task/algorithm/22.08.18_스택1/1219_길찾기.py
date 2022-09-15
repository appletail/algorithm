import sys
sys.stdin = open("input.txt", "r")


def dfs(s, g):
    v = s
    stack = [v]
    visited = [False] * 100
    visited[v] = True

    while stack:
        v = stack.pop()
        if v == g:
            return 1
        visited[v] = True
        for i in nodes[v]:
            if not visited[i]:
                stack.append(i)

    return 0


T = 10

for test_case in range(1, T + 1):
    t, V = map(int, input().split())

    nodes = []
    for _ in range(100):
        nodes.append([])

    node = list(map(int, input().split()))

    for i in range(0, len(node), 2):
        nodes[node[i]].append(node[i + 1])

    print(f'#{test_case} {dfs(0, 99)}')
