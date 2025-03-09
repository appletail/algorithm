import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def mkTree(current, parent):
    treeCnt[current] += 1
    for child in Ulst[current]:
        if child != parent:
            mkTree(child, current)
            treeCnt[current] += treeCnt[child]


N, R, Q = map(int, input().split())
Ulst = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    Ulst[U].append(V)
    Ulst[V].append(U)

Qlst = [int(input()) for _ in range(Q)]

treeCnt = [0] * (N+1)
mkTree(R, 0)

for q in Qlst:
    print(treeCnt[q])


# 다른 풀이
# def other():
#     input = sys.stdin.read
#     data = input().split()
#
#     idx = 0
#     N = int(data[idx])
#     R = int(data[idx + 1])
#     Q = int(data[idx + 2])
#     idx += 3
#
#     # 트리 구성
#     graph = [[] for _ in range(N + 1)]
#     for _ in range(N - 1):
#         U = int(data[idx])
#         V = int(data[idx + 1])
#         graph[U].append(V)
#         graph[V].append(U)
#         idx += 2
#
#     # 서브트리 크기 계산
#     size = [0] * (N + 1)
#
#     def dfs(node, parent):
#         size[node] = 1  # 자신도 포함
#         for child in graph[node]:
#             if child != parent:
#                 dfs(child, node)
#                 size[node] += size[child]
#
#     dfs(R, -1)  # 루트에서 시작
#
#     # 쿼리 처리
#     for _ in range(Q):
#         U = int(data[idx])
#         print(size[U])
#         idx += 1
#
# other()