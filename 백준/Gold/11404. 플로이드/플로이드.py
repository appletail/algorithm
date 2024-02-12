import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e10
nodes = [[INF] * n for _ in range(n)]
for i in range(n):
    nodes[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    nodes[a - 1][b - 1] = min(nodes[a - 1][b - 1], c)


for k in range(n):
    for s in range(n):
        for e in range(n):
            nodes[s][e] = min(nodes[s][k] + nodes[k][e], nodes[s][e])

for i in range(n):
    print(*[0 if x == INF else x for x in nodes[i]])
