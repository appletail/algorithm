import sys
sys.stdin = open("input.txt", "r")


def bfs():
    visited = [-1] * (v + 1)
    q = list()
    q.append(s)
    visited[s] = 0
    while q:
        tmp = q.pop(0)
        if tmp == g:
            return visited[g]
        for i in node[tmp]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[tmp] + 1
    return 0


T = int(input())

for test_case in range(1, T + 1):
    v, e = map(int, input().split())    # v노드 수, e간선 정보 수
    node = [[] for _ in range(v + 1)]

    for _ in range(e):
        n, w = map(int, input().split())
        node[n].append(w)
        node[w].append(n)

    s, g = map(int, input().split())

    result = bfs()
    print(f'#{test_case}', result)