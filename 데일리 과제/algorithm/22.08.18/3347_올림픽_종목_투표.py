import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))

    count = [0] * n

    for i in bi:
        for j in range(n):
            if ai[j] <= i:
                count[j] += 1
                break

    maxV = 0
    result = 0

    for k in range(n):
        if count[k] > maxV:
            maxV = count[k]
            result = k

    print(f'#{test_case} {result + 1}')
