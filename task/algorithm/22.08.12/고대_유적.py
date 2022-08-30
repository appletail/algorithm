import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    pic = [list(map(int, input().split())) for _ in range(n)]

    maxv = 0

    for row in range(n):
        for col in range(m):

            if pic[row][col] == 0:
                continue
            else:
                cnt = 0
                new_row = row
                new_col = col
                if col < m and pic[row][col] == 1:
                    while new_col < m and pic[new_row][new_col] == 1:
                        new_col += 1
                        cnt += 1

                if maxv < cnt:
                    maxv = cnt

                cnt = 0
                new_row = row
                new_col = col
                if row < n and pic[row][col] == 1:
                    while new_row < n and pic[new_row][new_col] == 1:
                        new_row += 1
                        cnt += 1

                if maxv < cnt:
                    maxv = cnt
    print(f'#{test_case} {maxv}')

# 다른 답
# 행탐색 열탐색하면 됨