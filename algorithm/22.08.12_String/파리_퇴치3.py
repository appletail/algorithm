import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    maxv = 0
       #  우 하  좌  상  우상 우하 좌하 좌상
    dr = [0, 1, 0, -1, -1, 1, 1, -1]
    dc = [1, 0, -1, 0, 1, 1, -1, -1]

    maxv = 0

    for b_row in range(n):
        for b_col in range(n):

            sumv = 0
            for i in range(4):  # 델타
                for j in range(1, m):  # 디스턴스
                    if 0 <= b_row + (dr[i] * j) < n and 0 <= b_col + (dc[i] * j) < n:
                        sumv += board[b_row + (dr[i] * j)][b_col + (dc[i] * j)]
            sumv += board[b_row][b_col]
            if maxv < sumv:
                maxv = sumv

            sumv = 0
            for i in range(4, 8): # 델타
                for j in range(1, m):  # 디스턴스
                    if 0 <= b_row + (dr[i] * j) < n and 0 <= b_col + (dc[i] * j) < n:
                        sumv += board[b_row + (dr[i] * j)][b_col + (dc[i] * j)]
            sumv += board[b_row][b_col]
            if maxv < sumv:
                maxv = sumv


    print(f'#{test_case} {maxv}')
