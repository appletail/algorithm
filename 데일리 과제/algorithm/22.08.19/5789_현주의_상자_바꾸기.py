import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    box = [0] * n

    for i in range(q):
        l, r = map(int, input().split())
        for idx in range(l - 1, r):
            box[idx] = i + 1

    print(f'#{test_case}', *box)
