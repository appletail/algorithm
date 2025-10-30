def isSurface(containerLoc, check):
    r, c = containerLoc
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if check[nr][nc] == 2:
            return True
    return False


def dfs(check):
    n, m = len(check), len(check[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    stack = [[0, 0]]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and check[nr][nc] == 2 or check[nr][nc] == 0:
                    visited[nr][nc] = 1
                    stack.append([nr, nc])
                    if check[nr][nc] == 0:
                        check[nr][nc] = 2

    
def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    check = [[2] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            check[i][j] = 1
    
    for request in requests:
        tmp = []
        isDouble = True
        if len(request) == 1:
            isDouble = False
        container = request[0]
        
        for i in range(n):
            for j in range(m):
                if storage[i][j] == container:
                    if isDouble:
                        tmp.append([i+1, j+1])
                    else:
                        if isSurface([i+1, j+1], check):
                            tmp.append([i+1, j+1])
        for r, c in tmp:
            check[r][c] = 0
        dfs(check)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if check[i][j] == 1:
                answer += 1
        
    return answer