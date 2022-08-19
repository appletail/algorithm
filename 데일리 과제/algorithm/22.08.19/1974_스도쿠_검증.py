import sys
sys.stdin = open("input.txt", "r")


def check_doku(arr):
    # 가로, 세로
    for i in range(9):
        check_garo = [0] * 10
        check_sero = [0] * 10
        for j in range(9):
            check_garo[arr[i][j]] += 1
            check_sero[arr[j][i]] += 1
        for k in range(10):
            if check_garo[k] > 1 or check_sero[k] > 1:
                return 0
    # 네모
    for rs in range(0, 9, 3):  # 행시작
        for cs in range(0, 9, 3):  # 열시작
            check_nemo = [0] * 10
            for r in range(3):  # 행
                for c in range(3):  # 열
                    check_nemo[arr[rs + r][cs + c]] += 1
            for k in range(10):
                if check_nemo[k] > 1:
                    return 0
    return 1


T = int(input())
# 가로 세로 네모 각각 다 돌면서 중복되거나 없는 숫자가 있는지 확인
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{test_case} {check_doku(sudoku)}')
