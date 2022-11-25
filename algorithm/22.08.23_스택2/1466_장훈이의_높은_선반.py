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
            result[k] = 1
            par(k + 1, midsum)
            result[k] = 0
            par(k + 1, midsum)


T = int(input())

for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    [1, 2, 3, 4, 5]
    [1, 1, 1, 0, 0]
    minV = 1e10
    result = [0] * n
    par(0)
    print(f'#{test_case} {minV - b}')
