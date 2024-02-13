import sys
input = sys.stdin.readline


def bfs(a, b):
    visited[a][b] = 1
    q = [(a, b)]

    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        c, d = q.pop(0)
        for dc, dd in dt:
            nc, nd = c + dc, d + dd
            if 0 <= nc < n and 0 <= nd < m:
                if arr[nc][nd] == 1 and visited[nc][nd] == 0:
                    q.append((nc, nd))
                    visited[nc][nd] = 1


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    result = 0

    for r in range(n):
        for c in range(m):
            if visited[r][c] == 0 and arr[r][c] == 1:
                bfs(r, c)
                result += 1

    print(result)
