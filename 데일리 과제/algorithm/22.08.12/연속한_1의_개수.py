import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    n_lst = list(map(int, input()))

    cnt = 0
    maxv = 0
    for i in n_lst:
        if i == 1:
            cnt += 1
        else:
            if maxv < cnt:
                maxv = cnt
            cnt = 0

    if maxv < cnt:
        maxv = cnt
    print(f'#{test_case} {maxv}')