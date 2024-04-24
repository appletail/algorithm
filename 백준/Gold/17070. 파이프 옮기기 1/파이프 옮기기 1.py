import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(N + 1)]  # 가로, 세로, 대각
for i in range(1, N):
    if house[0][i] == 1:
        break
    dp[0][i][0] = 1

for r in range(1, N):
    for c in range(N):
        if house[r][c] == 1:
            continue
        left, upper, upperLeft = 0, 0, 0
        leftWall, upperWall, upperLeftWall = house[r][c - 1], house[r - 1][c], house[r - 1][c - 1]
        if not leftWall:
            left += dp[r][c - 1][0] + dp[r][c - 1][2]
        if not upperWall:
            upper += dp[r - 1][c][1] + dp[r - 1][c][2]
        if not leftWall and not upperWall and not upperLeftWall:
            upperLeft += sum(dp[r - 1][c - 1])

        dp[r][c] = [left, upper, upperLeft]

print(sum(dp[N - 1][N - 1]))