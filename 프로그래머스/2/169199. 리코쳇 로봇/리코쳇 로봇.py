from collections import deque

def solution(board):
    N, M = len(board), len(board[0])
    R, G = [-1, -1], [-1, -1]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R = [i, j]
            elif board[i][j] == 'G':
                G = [i, j]
    
    visited = [[0] * M for _ in range(N)]
    visited[R[0]][R[1]] = 1
    q = deque([R])
    
    while q:
        r, c = q.popleft()
        if r == G[0] and c == G[1]:
            return visited[r][c] - 1
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            multi = 1
            while True:
                nr, nc = r + dr * multi, c + dc * multi
                if N <= nr or nr < 0 or M <= nc or nc < 0 or board[nr][nc] == 'D':
                    cr, cc = r + dr * (multi-1), c + dc * (multi-1)
                    if not visited[cr][cc]:
                        visited[cr][cc] = visited[r][c] + 1
                        q.append([cr, cc])
                    break
                multi += 1
                
    return -1
