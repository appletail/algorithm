# def par(k):  # 완전 검색(모든 부분집합)
#     if k == N:
#         print(result)
#         for i in range(N):
#             if result[i] == 1:
#                 print(lst[i], end=' ')
#         print()
#     else:
#         for i in range(2):
#             result[k] = i
#             par(k + 1)
#
#
# lst = [3, 4, 7]
# N = len(lst)
# result = [-1] * N
# par(0)


# def par(k):  # 완전 검색을 통한 특정 덧셈 구하기
#     if k == N:
#         sumV = 0
#         for i in range(N):
#             if result[i] == 1:
#                 sumV += lst[i]
#         if sumV == 12:
#             for i in range(N):
#                 if result[i] == 1:
#                     print(lst[i], end=' ')
#             print()
#     else:
#         for i in range(2):
#             result[k] = i
#             par(k + 1)
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(lst)
# result = [-1] * N
# par(0)


# def par(k, curSum):  # 백트래킹을 활용한 특정 덧셈 구하기
#     if curSum > 40:
#         print(k, '이상 탐색 안함', result)
#         return
#     if k == N:
#         if curSum == 40:
#             print(result)
#             for i in range(N):
#                 if result[i] == 1:
#                     print(lst[i], end=' ')
#             print()
#     else:
#         for i in range(2):
#             result[k] = i
#             if i:
#                 par(k + 1, curSum + lst[k])
#             else:
#                 par(k + 1, curSum)
#
#
# lst = [40, 20, 30, 10]
# N = len(lst)
# result = [-1] * N
# par(0, 0)


def per(k):  # 완전검색 순열
    if k == N:
        print(result)
        for i in result:
            print(lst[i], end=' ')
        print()
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                result[k] = i
                per(k + 1)
                visited[i] = False


lst = [10, 20, 30]
N = len(lst)
result = [-1] * N
visited = [False] * N
per(0)
