from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    q = deque([(0, 0)])
    visited[0][0] = 1
    
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == m - 1:
            answer = visited[n - 1][m - 1]
            break
            
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    
    return answer