import sys
sys.stdin = open("input.txt", "r")


def boong_eh(m, k, arr):
    count = [0] * 11112
    for customer in arr:
        count[customer] += 1

    fish_bread = 0
    c_sum = 0
    for second in range(11112):
        if second >= m and second % m == 0:
            fish_bread += k
        c_sum += count[second]
        if c_sum > fish_bread:
            return 'Impossible'

    return 'Possible'


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    c_lst = list(map(int, input().split()))
    # n명이 오고 m초 단위로 k개 만들 수 있음

    print(f'#{test_case} {boong_eh(M, K, c_lst)}')
