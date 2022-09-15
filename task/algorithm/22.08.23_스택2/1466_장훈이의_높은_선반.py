import sys
sys.stdin = open("input.txt", "r")


def par(k):
    global minV
    if minV == b:
        return
    if k == n:
        sumV = 0
        for i in range(n):
            if result[i] == 1:
                sumV += lst[i]
        if b <= sumV < minV:
            minV = sumV
    else:
        for i in range(2):
            result[k] = i
            par(k + 1)


T = int(input())

for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))

    minV = 1e10
    result = [0] * n
    par(0)
    print(f'#{test_case} {minV - b}')
