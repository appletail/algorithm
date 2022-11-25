import sys
sys.stdin = open("input.txt", "r")


def check():
    result = 0
    for r in range(n):
        for c in range(n):
            ks = [0] * (max_k + 1)
            for y, x in homes:
                k = abs(c - x) + 1 + abs(y - r)
                ks[k] += 1
            for i in range(1, max_k + 1):
                ks[i] += ks[i - 1]
                margin = (ks[i] * m) - (i ** 2 + (i - 1) ** 2)
                if margin >= 0:
                    result = max(result, ks[i])
    return result


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    max_k = 2 * n - 1
    board = [list(map(int, input().split())) for _ in range(n)]
    homes = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                homes.append((i, j))

    print(f'#{test_case}', check())
