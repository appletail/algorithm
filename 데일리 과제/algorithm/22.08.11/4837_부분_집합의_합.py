import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):
        arr = []
        for j in range(12):
            if i & (1 << j):
                arr.append(j + 1)
        if len(arr) == n and sum(arr) == k:
            print(arr)
            cnt += 1

    print(f'#{test_case} {cnt}')


# sum 말고 누적하는 방식으로 계산하도록 수정할 것