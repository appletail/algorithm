import sys
sys.stdin = open("input.txt", "r")


# def inorder(root):
#     if int(tree[root][1]) != 0:
#         inorder(int(tree[root][1]))
#     print(tree[root][0], end='')
#     if int(tree[root][2]) != 0:
#         inorder(int(tree[root][2]))
#
#
# T = 10
#
# for test_case in range(1, T + 1):
#     n = int(input())
#     tree = [[0, 0, 0] for _ in range(n + 1)]
#
#     tmp = [list(input().split()) for _ in range(n)]
#     for i in tmp:
#         for j in range(1, len(i)):
#             tree[int(i[0])][j - 1] = i[j]
#     print(f'#{test_case}', end=' ')
#     inorder(1)
#     print()


# 다른 답
def inorder(root):
    if root:    # root가 0이 아니라는 뜻
        inorder(int(tree[root][1]))
        print(tree[root][0], end='')
        inorder(int(tree[root][2]))


T = 10

for test_case in range(1, T + 1):
    n = int(input())
    tree = [[0, 0, 0] for _ in range(n + 1)]

    tmp = [list(input().split()) for _ in range(n)]
    for i in tmp:
        for j in range(1, len(i)):
            tree[int(i[0])][j - 1] = i[j]
    print(f'#{test_case}', end=' ')
    inorder(1)
    print()

