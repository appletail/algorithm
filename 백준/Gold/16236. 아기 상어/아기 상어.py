import sys
input = sys.stdin.readline
from collections import deque


def bfs(shark, lg):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((shark[0], shark[1]))
    visited[shark[0]][shark[1]] = 0
    results = []
    while q and lg:
        r, c = q.popleft()
        if (r, c) in goal and board[r][c]:
            results.append((r, c, visited[r][c]))
            lg -= 1
        else:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] <= size and visited[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
    if results:
        results.sort(key=lambda x: (x[2], x[0], x[1]))
        return results[0]
    else:
        return 0, 0, 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
fish = []
baby = [0, 0]
length = 0
for i in range(n):
    for j in range(n):
        if board[i][j] and board[i][j] != 9:
            fish.append((board[i][j], i, j))
            length += 1
        elif board[i][j] == 9:
            baby = [i, j]
            board[i][j] = 0
fish.sort(reverse=True)

size = 2
eat = 0
time = 0
goal = []
lg = 0
while True:
    for i in range(length - 1, -1, -1):
        if fish[i][0] < size:
            tmp, fr, fc = fish.pop()
            goal.append((fr, fc))
            lg += 1
            length -= 1
        else:
            break

    baby[0], baby[1], plus = bfs(baby, lg)
    if not plus:
        break
    else:
        board[baby[0]][baby[1]] = 0
        time += plus
        lg -= 1
        eat += 1
        if eat == size:
            size += 1
            eat = 0

print(time)