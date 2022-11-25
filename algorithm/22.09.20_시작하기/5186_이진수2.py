import sys
sys.stdin = open("input.txt", "r")


# T = int(input())
# for test_case in range(1, T + 1):
#     n = float(input())
#
#     result = ''
#     cnt = 1
#     while n > 0 and cnt < 13:
#         n *= 2
#         if n >= 1:
#             result += '1'
#             n -= 1
#         else:
#             result += '0'
#         cnt += 1
#
#     print(f'#{test_case}', end=' ')
#     if n:
#         print('overflow')
#     else:
#         print(result)

# 다른 답
T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = float(input())
    res = ''
    for power in range(-1, -13, -1):
        if N >= 2**power:
            res += '1'
            N -= 2**power
        else:
            if N == 0:
                break
            res += '0'
    print('overflow') if N > 0 else print(res)
