# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
#
# def findRoot(idx):
#     union[idx] = findRoot(union[idx]) if union[idx] != idx else idx
#     return union[idx]
#
#
# V, E = map(int, input().split())
# nodes = [list(map(int, input().split())) for _ in range(E)]
#
# nodes.sort(key=lambda x: x[2])
# union = [i for i in range(V+1)]
#
# answer = 0
# cnt = 0
# for A, B, C in nodes:
#     rootA, rootB = findRoot(A), findRoot(B)
#     if rootA != rootB:
#         answer += C
#         cnt += 1
#         if rootA > rootB:
#             union[rootA] = rootB
#         else:
#             union[rootB] = rootA
#
#         if cnt == V-1:
#             break
#
# print(answer)



import sys
input = sys.stdin.readline

def findRoot(idx):
    while union[idx] != idx:
        idx = union[idx]
    return idx

V, E = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(E)]

nodes.sort(key=lambda x: x[2])
union = [i for i in range(V+1)]

answer = 0
cnt = 0
for A, B, C in nodes:
    rootA, rootB = findRoot(A), findRoot(B)
    if rootA != rootB:
        answer += C
        cnt += 1
        if rootA > rootB:
            union[rootA] = rootB
        else:
            union[rootB] = rootA

        if cnt == V-1:
            break

print(answer)
