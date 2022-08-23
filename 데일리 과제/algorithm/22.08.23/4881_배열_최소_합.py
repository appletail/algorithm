import sys
sys.stdin = open("input.txt", "r")


def mini(k, curSum):
    global minV
    if curSum >= minV:
        return
    if k == n:
        if minV > curSum:
            minV = curSum
    else:
        for i in range(n):
            if not result[i]:
                result[i] = True
                mini(k + 1, curSum + arr[k][i])
                result[i] = False


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [False] * n
    minV = 999999999

    mini(0, 0)
    print(f'#{test_case} {minV}')
