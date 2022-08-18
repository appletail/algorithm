import sys
sys.stdin = open("input.txt", "r")


def dfs(s, g):
    v = s
    stack = [v]
    visited = [False] * (V + 1)
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


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    nodes = []
    for _ in range(V + 1):
        nodes.append([])

    for _ in range(E):
        n = list(map(int, input().split()))
        nodes[n[0]].append(n[1])

    S, G = map(int, input().split())

    print(f'#{test_case} {dfs(S, G)}')


# def dfsr(v):
#     visited[v] = True
#     if v == G
#         return 1
#     print(v, end=' ')
#     for w in G[v]:
#         if not visited[w]:
#             if dfsr(w) == 1:
#                 return 1
#     return 0