import sys
sys.stdin = open("input.txt", "r")


def rsp(st, ed):
    if st == ed:
        return st
    else:
        a = rsp(st, (st + ed)//2)
        b = rsp((st + ed) // 2 + 1, ed)
        if n_lst[a] == n_lst[b]:
            return a
        elif n_lst[a] == 1:
            if n_lst[b] == 2:
                return b
            elif n_lst[b] == 3:
                return a
        elif n_lst[a] == 2:
            if n_lst[b] == 1:
                return a
            elif n_lst[b] == 3:
                return b
        elif n_lst[a] == 3:
            if n_lst[b] == 1:
                return b
            elif n_lst[b] == 2:
                return a


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    n_lst = list(map(int, input().split()))

    print(f'#{test_case} {rsp(0, n - 1) + 1}')
