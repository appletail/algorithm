import sys
input = sys.stdin.readline

def prim():
    mst = [0] * N
    key = [1e100000] * N
    key[0] = 0
    for _ in range(N - 1):
        minV = 1e100000
        u = 0
        for i in range(N):
            if not mst[i] and key[i] < minV:
                u = i
                minV = key[i]
        mst[u] = 1

        for i in range(N):
            if not mst[i] and G[u][i]:
                key[i] = min(key[i], G[u][i])

    print(round(sum(key), 2))


N = int(input())
G = [[0] * N for _ in range(N)]
stars = [list(map(float, input().split())) for _ in range(N)]
for i in range(N - 1):
    x, y = stars[i]
    for j in range(i + 1, N):
        dx, dy = stars[j]
        w = ((x - dx) ** 2 + (y - dy) ** 2) ** 0.5
        G[i][j] = w
        G[j][i] = w
prim()
