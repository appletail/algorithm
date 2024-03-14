import sys
input = sys.stdin.readline
from collections import deque


def bfs(N, M, board):
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    q = deque([[0, 0, False]])
    while q:
        r, c, isBreak = q.popleft()
        if visited[N - 1][M - 1][0] != 0 or visited[N - 1][M - 1][1] != 0:
            return max(visited[N - 1][M - 1])
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    if not isBreak and not visited[nr][nc][0]:
                        visited[nr][nc][0] = visited[r][c][0] + 1
                        q.append([nr, nc, isBreak])
                    elif isBreak and not visited[nr][nc][1]:
                        visited[nr][nc][1] = visited[r][c][1] + 1
                        q.append([nr, nc, isBreak])
                elif board[nr][nc] == 1 and not isBreak:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    q.append([nr, nc, True])

    return -1

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(N, M, board))
