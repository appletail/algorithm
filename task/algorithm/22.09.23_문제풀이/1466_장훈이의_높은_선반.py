import sys
sys.stdin = open("input.txt", "r")


def sub(d, curS):
    global minV
    if minV == b:
        return

    if d == n:
        if minV > curS >= b:
            minV = curS
    else:
        sub(d + 1, curS + n_lst[d])
        sub(d + 1, curS)


T = int(input())
for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    n_lst = list(map(int, input().split()))
    minV = 1e10
    sub(0, 0)
    print(f'#{test_case}', minV - b)