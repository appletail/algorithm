import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

nodes = [[1e10] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    nodes[a - 1][b - 1] = min(nodes[a - 1][b - 1], c)

for i in range(n):
    nodes[i][i] = 0

for k in range(n):
    for s in range(n):
        for e in range(n):
            nodes[s][e] = min(nodes[s][k] + nodes[k][e], nodes[s][e])

for i in range(n):
    for j in range(n):
        if nodes[i][j] == 1e10:
            nodes[i][j] = 0

for i in range(n):
    print(*nodes[i])
