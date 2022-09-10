# import sys
# sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for test_case in range(1, T + 1):
    n, mink, maxk = map(int, input().split())   # 입력
    n_lst = list(map(int, input().split()))
    n_lst.sort()    # 정렬

    count = [0] * (n_lst[-1] + 1)    # 카운팅
    for i in n_lst:
        count[i] += 1

    end = n_lst[-1]

    result = 1e10

    for t1 in range(1, end):
        for t2 in range(t1 + 1, end + 1):
            a, b, c = 0, 0, 0
            # a 계산
            for aS in range(t2, end + 1):
                a += count[aS]
            if a < mink or a > maxk:
                continue
            # b 계산
            for bS in range(t1, t2):
                b += count[bS]
            if b < mink or b > maxk:
                continue
            # c 계산
            for cS in range(t1):
                c += count[cS]
            if c < mink or c > maxk:
                continue

            result = min(result, max(a, b, c) - min(a, b, c))

    if result == 1e10:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {result}')
