import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    maxv = 0
       # 우 하  좌  상            우상 우하 좌하 좌상
    dr = [0, 1, 0, -1, -2, -1, -2, 1, 2, 1, 2, -1, -2]
    dc = [1, 0, -1, 0, 0, 1, 2, 1, 2, -1, -2, ]


    for b_row in range(n):
        for b_col in range(n):

            sumv = 0

            for m_row in range(b_row, b_row + m):
                for m_col in range(b_col, b_col + m):
                    sumv += board[m_row][m_col]
            if sumv > maxv:
                maxv = sumv

    print(f'#{test_case} {maxv}')
