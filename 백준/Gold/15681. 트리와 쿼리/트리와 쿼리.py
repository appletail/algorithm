import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def mkTree(current, parent, treeCnt):
    treeCnt[current] += 1
    for child in Ulst[current]:
        if child != parent:
            tree[current].append(child)
            treeCnt[current] += mkTree(child, current, treeCnt)[child]

    return treeCnt


N, R, Q = map(int, input().split())
Ulst = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    Ulst[U].append(V)
    Ulst[V].append(U)

Qlst = [int(input()) for _ in range(Q)]

tree = [[] for _ in range(N+1)]
treeCnt = [0] * (N+1)
mkTree(R, 0, treeCnt)

for q in Qlst:
    print(treeCnt[q])
