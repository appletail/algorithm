import sys
sys.stdin = open("input.txt", "r")


def dfs(sr, sc, curS):
    global minV
    if minV < curS:
        return
    s = list()
    s.append((sr, sc))
    while s:
        r, c = s.pop()
        result = curS + board[r][c]
        if (r, c) == (N - 1, N - 1):
            if minV > result:
                minV = result
            return
        for dr, dc in dt:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                dfs(nr, nc, result)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    minV = 1e10
    dt = [(1, 0), (0, 1)]
    dfs(0, 0, 0)
    print(f'#{test_case}', minV)
#
#
# # 교수님 답
# def solve(r, c):
#     if r == goalR and c == goalC:
#         ...
#         return
#
#     if r + 1 이 영역 안일 때:
#         solve(r + 1, c)
#     if c + 1 이 영역 안일 때:
#         solve(r, c + 1)
#
# 이대로 풀면 시간초과가 나는데 백트래킹으로 해결해라
from collections import deque

dx = [1, 0]
dy = [0, 1]

def bfs(x, y, s):
    minv = (n ** 2) * 10

    q = deque()
    q.append((x, y, s))  # q에 담고

    while q:
        x, y, s = q.popleft()
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and s + arr[ny][nx] < minv:
                if nx == n-1 and ny == n-1:
                    minv = s + arr[ny][nx]
                else:
                    q.append((nx, ny, s + arr[ny][nx]))

    return minv


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = bfs(0,0,arr[0][0])
    print(f'#{tc} {ans}')