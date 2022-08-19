import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    ai = []
    bi = []
    cj = []

    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        ai.append(a)
        bi.append(b)

    p = int(input())
    for _ in range(p):
        cj.append(int(input()))

    result = [0] * 5001

    for i in range(n):
        for j in range(ai[i], bi[i] + 1):
            result[j] += 1

    print(f'#{test_case}', end=' ')
    for k in range(p - 1):
        print(result[cj[k]], end=' ')
    print(result[cj[p - 1]])

