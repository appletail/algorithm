import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    n_lst = list(map(int, input().split()))

    for i in range(10):
        tmp = n_lst[i]
        for j in range(i + 1, n):
            if i % 2 == 0 and tmp < n_lst[j]:       # 제일 작은 수
                tmp = n_lst[j]
                n_lst[i], n_lst[j] = n_lst[j], n_lst[i]
            elif i % 2 and tmp > n_lst[j]:           # 제일 큰 수
                tmp = n_lst[j]
                n_lst[i], n_lst[j] = n_lst[j], n_lst[i]

    print(f'#{test_case}', end=' ')
    print(*n_lst[0:10])

