import sys
sys.stdin = open("input.txt", "r")


def palin(arr):
    maxv = 1

    for i in range(100):  # 행
        for j in range(100):  # 열 시작점
            for k in range(100 - j, 1, -1):  # 길이
                if k <= maxv:
                    break
                for m in range(k // 2):
                    if arr[i][j + m] != arr[i][j + k - 1 - m]:
                        break
                else:
                    maxv = k

    return maxv


T = 10

for test_case in range(1, T + 1):
    a = input()
    garo_board = [list(input()) for _ in range(100)]
    sero_board = [list(l) for l in zip(*garo_board)]

    garo = palin(garo_board)
    sero = palin(sero_board)

    maxlen = max(garo, sero)


    print(f'#{test_case} {maxlen}')


# 다른 답
# def get_solution2(arr, m):  #문자열,
#     for word in arr:  # 1 ~ 100 열마다 가꼬옴
#         for s in range(100 - m + 1):    # 큰 수부터 체크
#             for k in range(m // 2):
#                 if word[s + k] != word[s + m - 1 - k]:
#                     break
#             else:
#                 return m
#     return 0
#
#
# T = 10
# for _ in range(1, T + 1):
#     t = int(input())        # 테스트 케이스
#     a = [input() for _ in range(100)]   # 문자열 배열
#     b = [''.join(x) for x in zip(*a)]   # 행열 바꿈
#
#     maxLength = 1
#     for m in range(2, 101):     # m == 문자열의 길이
#         if m > maxLength + 2: break
#         if maxLength < get_solution2(a, m):
#             maxLength = m
#
#     m = maxLength + 1
#     for m in range(maxLength + 1, 101):
#         if m > maxLength + 2: break
#         if maxLength < get_solution2(b, m):
#             maxLength = m
#
#     print('#%d %s' % (t, maxLength))