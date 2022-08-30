import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    a, b = input().split()
    n, m = len(a), len(b)

    cnt = 0
    i = 0

    while i < n:
        if a[i: i + m] == b:
            cnt += 1
            i += m      # a= babababa b = bab 인 경우 b가 중복하여 카운트 됨 그래서 i += m을 해줘야함
        else:
            i += 1

    print(f'#{test_case} {n - (m - 1) * cnt}')
