import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxv = 0
    right = left =0
    for i in range(100):
        garo = sero = 0
        for j in range(100):

            garo += arr[i][j]
            if garo > maxv:
                maxv = garo

            sero += arr[j][i]
            if sero > maxv:
                maxv = sero

            if i == j:
                right += arr[i][j]

            if i + j == 100:
                left += arr[i][j]

    if right > maxv:
        maxv = right
    if left > maxv:
        maxv = left

    print(f'#{test_case} {maxv}')