# 제출한 답 - 620ms

# import sys
# from collections import deque
# input = sys.stdin.readline
#
#
# def updateOutside(start):
#     r, c = start
#     q = deque()
#     q.append((r, c))
#     outside[r*M+c] = 1
#
#     while q:
#         r, c = q.popleft()
#         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M:
#                 if paper[nr][nc] == 0 and not outside[nr*M+nc]:
#                     q.append((nr, nc))
#                     outside[nr*M+nc] = 1
#
#
# N, M = map(int, input().split())
# paper = [list(map(int, input().split())) for _ in range(N)]
#
# # 치즈 위치 확인
# # outside 확인
# # 치즈 녹임
# # 녹은 치즈를 기준으로 outside 갱신
# # outside 갱신
#
# cheese = []
# outside = [0] * (N * M)
# time = 0
# for i in range(N):
#     for j in range(M):
#         if paper[i][j] == 1:
#             cheese.append((i, j))
#
# updateOutside((0, 0))
#
# while cheese:
#     time += 1
#     leftover = []
#     melted = []
#     for r, c in cheese:
#         cnt = 0
#         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             nr, nc = r + dr, c + dc
#             if outside[nr*M+nc]:
#                 cnt += 1
#         if cnt < 2:
#             leftover.append((r, c))
#         else:
#             melted.append((r, c))
#     cheese = leftover
#     for r, c in melted:
#         updateOutside((r, c))
#
# print(time)


# 다른 사람 - 40ms
import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    board[0][0] = -1
    queue = [(0, 0)]
    time = -1
    while queue:
        _queue = []
        while queue:
            r, c = queue.pop(0)
            for dr, dc in delta:
                if N > r+dr >= 0 and M > c+dc >= 0:
                    if board[r+dr][c+dc] < 0:
                        continue
                    if board[r+dr][c+dc] == 0:
                        queue.append((r+dr, c+dc))
                        board[r+dr][c+dc] = -1
                    elif board[r+dr][c+dc] == 1:
                        board[r+dr][c+dc] += 1
                    else:
                        _queue.append((r+dr, c+dc))
                        board[r+dr][c+dc] = -1
        queue = _queue
        time += 1
    print(time)

solution()