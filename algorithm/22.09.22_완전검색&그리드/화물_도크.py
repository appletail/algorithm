import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    time = sorted(time, key=lambda x: x[1])

    cnt = 1
    current = time[0]
    for i in range(1, n):
        if time[i][0] >= current[1]:
            cnt += 1
            current = time[i]

    print(f'#{test_case}', cnt)