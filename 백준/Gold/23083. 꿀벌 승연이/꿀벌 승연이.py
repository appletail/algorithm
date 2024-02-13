import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hive = [[0] * M for _ in range(N)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    hive[x - 1][y - 1] = -1
hive[0][0] = 1
delta = {
    0: [(-1, 0), (0, -1), (-1, -1)],
    1: [(-1, 0), (0, -1), (1, -1)]
}
for c in range(M):
    for r in range(N):
        if hive[r][c] >= 0:
            for dr, dc in delta.get(c % 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and hive[nr][nc] >= 0:
                    hive[r][c] += hive[nr][nc]

print(hive[N - 1][M - 1] % int((1e9 + 7)))
