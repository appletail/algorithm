import sys
input = sys.stdin.readline


def dfs(r, c, cnt, sumV):
    global result
    visited[r][c] = 1
    if result >= sumV + (4 - cnt) * maxV:
        return

    if cnt == 4:
        result = max(result, sumV)
    else:
        for dr, dc in [(1, 0), (-1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    dfs(nr, nc, cnt + 1, sumV + paper[nr][nc])
                    if cnt == 2:
                        dfs(r, c, cnt + 1, sumV + paper[nr][nc])
                    visited[nr][nc] = 0


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
maxV = max(map(max, paper))

result = 0
for i in range(n):
    for j in range(m):
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = 0

print(result)
