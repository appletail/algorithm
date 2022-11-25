import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    n_lst = list(map(int, input().split()))

    cnt = 1
    maxv = 1

    for i in range(n - 1):
        if n_lst[i] + 1 == n_lst[i + 1]:
            cnt += 1
        else:
            if maxv < cnt:
                maxv = cnt
            cnt = 1
        if maxv < cnt:
            maxv = cnt

    print(f'#{test_case} {maxv}')