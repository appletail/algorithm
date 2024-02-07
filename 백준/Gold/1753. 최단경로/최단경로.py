import sys
input = sys.stdin.readline
import heapq


V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])

heap = []
heapq.heappush(heap, [0, K])

visited = [0] * (V + 1)
distance = ['INF'] * (V + 1)
distance[K] = 0
while heap:
    d, u = heapq.heappop(heap)
    visited[u] = 1
    for v, w in G[u]:
        if not visited[v]:
            if distance[v] == 'INF' or distance[v] > d + w:
                distance[v] = d + w
                heapq.heappush(heap, [distance[v], v])

for answer in distance[1:]:
    print(answer)
