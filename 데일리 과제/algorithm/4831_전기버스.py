import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 갈 수 있는 범위 내에서 가장 바깥에 있는 충전소 충전
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    stop = [0] * (N + 1)
    for i in charge:
        stop[i] += 1

    cnt = 0
    pos = 0
    while pos + K < N:
        if 1 in stop[pos + 1: pos + K + 1]:
            cnt += 1
            plus = 0
            for j in range(K):
                if stop[pos + 1: pos + K + 1][j] == 1:
                    plus = j
            pos += plus + 1

        else:
            cnt = 0
            break

    print(f'#{test_case} {cnt}')
