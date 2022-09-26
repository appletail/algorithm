import sys
sys.stdin = open("input.txt", "r")

dt = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def solve(k, r, c, d):
    global maxV

    if d == 3 and r == stR and c == stC:
        if maxV < k:
            maxV = k
        return

    # if r하고 c가 범위를 벗어나거나 같은 디저트면:
    if r < 0 or r >= N or c < 0 or c >= N or board[r][c] in result[:k]:
        return

    result[k] = board[r][c]
    newR, newC = r + dt[d][0], c + dt[d][1]
    solve(k + 1, newR, newC, d)
    d = (d + 1) % 4
    newR, newC = r + dt[d][0], c + dt[d][1]
    solve(k + 1, newR, newC, d)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    maxV = -1

    for r in range(N):
        for c in range(N):
            stR,stC = r, c
            result = [-1] * (4 * N)
            solve(0, r, c, 0)

    print(f'#{test_case}', maxV)