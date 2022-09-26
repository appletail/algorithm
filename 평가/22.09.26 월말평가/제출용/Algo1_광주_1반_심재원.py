T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 지형의 수
    bong = list(map(int, input().split()))

    # flag가 1에서 0으로 바뀌면 봉으로 판단
    cnt = 0
    flag = 1
    for i in range(1, N):
        if bong[i] > bong[i - 1] and not flag:
            flag = 1
        elif bong[i] < bong[i - 1] and flag:
            flag = 0
            cnt += 1

    # 마지막 지형이 앞의 것보다 큰지 확인
    if flag:
        cnt += 1

    print(f'#{test_case}', cnt)
