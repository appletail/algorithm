import sys
sys.stdin = open("input.txt", "r")


# T = int(input())
#
# for test_case in range(1, T + 1):
#     n = int(input())
#     n_lst = list(map(int, input().split()))
#
#     result = 0
#
#     while len(n_lst) > 0:
#         max_idx = n_lst.index(max(n_lst))
#         result += max(n_lst) * len(n_lst[:max_idx]) - sum(n_lst[:max_idx])
#         n_lst = n_lst[max_idx + 1:]
#
#     print(f'#{test_case} {result}')



# tc = int(input())
#
# for t in range(1, tc + 1):
#     n = int(input())
#     prices = list(map(int, input().split()))
#     benefits, answer = 0, 0
#
#     while len(prices) > 0:
#         max_idx = prices.index(max(prices))
#         temp = prices[:max_idx + 1]
#         prices = prices[max_idx + 1:]
#         benefits += temp[-1] * (len(temp) - 1) - sum(temp[:-1])
#
#     print(f'#{t} {benefits}')


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nLst = list(map(int, input().split()))  # 2 5 9 =-> 9 5 2 11

    maxV = nLst[-1]     # 최대값
    total = 0

    for i in range(len(nLst) - 2, -1, -1): # 최대값 다음부터
        if maxV < nLst[i]:      # 최대값 갱신
            maxV = nLst[i]
        else:
            total += maxV - nLst[i]  # 최대값이 아니라면 최대값과 그 아래 요소의 차만큼 더함

    print(f'#{test_case} {total}')