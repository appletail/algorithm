import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nongjang = [input() for _ in range(n)]

    result = 0

    for i in range(n):
        result += int(nongjang[n // 2][i])

    row_up = n // 2 - 1
    row_down = n // 2 + 1
    col = 1
    col_len = n - 2
    while row_down < n:
        # 위
        for j in range(col, col + col_len):
            result += int(nongjang[row_up][j])

        # 아래
        for j in range(col, col + col_len):
            result += int(nongjang[row_down][j])

        row_up -= 1
        row_down += 1
        col += 1
        col_len -= 2

    print(f'#{test_case} {result}')
