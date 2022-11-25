# import sys
# sys.stdin = open("input.txt", "r")
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     n = int(input())
#
#     pascal_lst = []
#     for i in range(n):
#         tmp = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 tmp.append(1)
#             else:
#                 tmp.append(pascal_lst[i - 1][j] + pascal_lst[i - 1][j - 1])
#         pascal_lst.append(tmp)
#
#     print(f'#{test_case}')
#     for k in range(n):
#         for m in range(k + 1):
#             print(pascal_lst[k][m], end=' ')
#         print()


import sys
sys.stdin = open("input.txt", "r")


pascal_lst = []
for i in range(10):
    tmp = []
    for j in range(i + 1):
        if j == 0 or j == i:
            tmp.append(1)
        else:
            tmp.append(pascal_lst[i - 1][j] + pascal_lst[i - 1][j - 1])
    pascal_lst.append(tmp)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    print(f'#{test_case}')
    for k in range(n):
        for m in range(k + 1):
            print(pascal_lst[k][m], end=' ')
        print()