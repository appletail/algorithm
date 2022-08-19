import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    word_puzzle = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for r in range(n):
        cnt_garo = 0
        cnt_sero = 0
        for c in range(n):
            # 가로
            if word_puzzle[r][c] == 1:
                cnt_garo += 1
            else:
                if cnt_garo == k:
                    result += 1
                cnt_garo = 0
            # 세로
            if word_puzzle[c][r] == 1:
                cnt_sero += 1
            else:
                if cnt_sero == k:
                    result += 1
                cnt_sero = 0
        else:
            if cnt_garo == k:
                result += 1
            if cnt_sero == k:
                result += 1

    print(f'#{test_case}', result)
