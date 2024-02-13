import sys
input = sys.stdin.readline
import heapq


def dijkstra(g, n, x):
    distance = [1e10] * (n + 1)
    distance[x] = 0

    heap = []
    heapq.heappush(heap, [0, x])

    visited = [0] * (n + 1)
    while heap:
        w, u = heapq.heappop(heap)
        visited[u] = 1
        for v, t in g[u]:
            if not visited[v]:
                newW = w + t
                if distance[v] > newW:
                    distance[v] = newW
                    heapq.heappush(heap, [newW, v])

    return distance


N, M, X = map(int, input().split())

go = [[] for _ in range(N + 1)]
back = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    go[A].append([B, T])
    back[B].append([A, T])

goTime = dijkstra(go, N, X)
backTime = dijkstra(back, N, X)

answer = 0
for i in range(1, N + 1):
    times = goTime[i] + backTime[i]
    if times > answer:
        answer = times

print(answer)
