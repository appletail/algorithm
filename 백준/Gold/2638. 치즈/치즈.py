import sys
from collections import deque
input = sys.stdin.readline


def updateOutside(start):
    r, c = start
    q = deque()
    q.append((r, c))
    outside[r*M+c] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if paper[nr][nc] == 0 and not outside[nr*M+nc]:
                    q.append((nr, nc))
                    outside[nr*M+nc] = 1


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

cheese = []
outside = [0] * (N * M)
time = 0
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            cheese.append((i, j))

updateOutside((0, 0))

while cheese:
    time += 1
    leftover = []
    melted = []
    for r, c in cheese:
        cnt = 0
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if outside[nr*M+nc]:
                cnt += 1
        if cnt < 2:
            leftover.append((r, c))
        else:
            melted.append((r, c))
    cheese = leftover
    for r, c in melted:
        updateOutside((r, c))

print(time)
