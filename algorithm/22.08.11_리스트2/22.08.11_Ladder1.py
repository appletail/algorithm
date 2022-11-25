import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    col = 0

    for i in range(100):
        if ladder[-1][i] == 2:
            col += i
            break

    for up in range(100):
        row = 99 - up

        if 0 < col and ladder[row][col - 1] == 1:
            while 0 < col and ladder[row][col - 1] == 1: # 좌
                col -= 1
        elif col < 99 and ladder[row][col + 1] == 1:
            while col < 99 and ladder[row][col + 1] == 1:
                col += 1

    print(f'#{test_case} {col}')