import sys
input = sys.stdin.readline
from collections import deque

dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(arr):
    q = deque()
    for r, c in arr:
        q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in dt:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not box[nr][nc]:
                box[nr][nc] = box[r][c] + 1
                q.append((nr, nc))

    maxV = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
            else:
                maxV = max(maxV, box[i][j])

    return maxV - 1


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
start = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            start.append((i, j))

print(bfs(start))
