import sys
input = sys.stdin.readline


def bfs():
    visited = [[0] * m for _ in range(n)]
    q = [(0, 0)]
    dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[0][0] = 1
    cnt = 0

    while q:
        r, c = q.pop(0)

        if r == n - 1 and c == m - 1:
            return visited[r][c]

        for dr, dc in dt:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    return -1


n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs())