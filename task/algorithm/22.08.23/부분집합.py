# def par(k):
#     if k == N:
#         print(result)
#         # return
#     else:
#         for i in range(2):
#             result[k] = i
#             par(k + 1)

# def par(k):  # 완전검색
#     if k == N:
#         print(result)
#         sumV = 0
#         for i in range(N):
#             if result[i] == 1:
#                 sumV += lst[i]
#         if sumV == 40:
#             for i in range(N):
#                 if result[i] == 1:
#                     print(lst[i], end=' ')
#             print()
#     else:
#         result[k] = 0
#         par(k + 1)
#
#         result[k] = 1
#         par(k + 1)
#
#
# lst = [10, 30, 40]
# N = len(lst)
# result = [-1] * N
# par(0)

# def par(k, curSum):
#     print(k, result)
#     if curSum > 40:  # 백트래킹 하는 부분
#         # print('이상', k, result)
#         return
#
#     if k == N:
#         if curSum == 40:
#             for i in range(N):
#                 if result[i] == 1:
#                     print(lst[i], end=' ')
#             print()
#     else:
#         result[k] = 0
#         par(k + 1, curSum)
#
#         result[k] = 1
#         par(k + 1, curSum + lst[k])
#
#
# lst = [40, 10, 20, 30]
# N = 4
# result = [-1] * N
# par(0, 0)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(lst)
# result = [-1] * N
# par(0, 0)


def per(k):  # 완전검색 순열
    if k == N:
        print(result)
        for i in range(N):
            print(lst[result[i]], end=' ')
        print()
        return

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
