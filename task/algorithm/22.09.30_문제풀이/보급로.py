import sys
sys.stdin = open("input.txt", "r")


def solve():
    Q = []
    Q.append((0, 0))
    while Q:
        row, col = Q.pop(0)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nR, nC = row + dr, col + dc
            if 0 <= nR < N and 0 <= nC < N and D[nR][nC] > D[row][col] + ARR[nR][nC]:
                D[nR][nC] = D[row][col] + ARR[nR][nC]
                Q.append((nR, nC))


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    ARR = [list(map(int, input())) for _ in range(N)]

    D = [[1e10] * N for _ in range(N)]
    D[0][0] = 0
    solve()
    print(f'#{tc}', D[-1][-1])