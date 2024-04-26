import sys
input = sys.stdin.readline
import heapq

def dijkstra(s, e):
    distance = [1e10] * (N + 1)
    distance[s] = 0

    heap = []
    heapq.heappush(heap, [distance[s], s])
    visited = [0] * (N + 1)
    while heap:
        curDist, curNode = heapq.heappop(heap)
        visited[curNode] = 1
        for nodeTo, dist in graph[curNode]:
            if not visited[nodeTo]:
                if distance[nodeTo] > (newDist:=curDist+dist):
                    distance[nodeTo] = newDist
                    heapq.heappush(heap, [newDist, nodeTo])

    return distance[e]

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    r, c, d = map(int, input().split())
    graph[r].append([c, d])
    graph[c].append([r, d])
v1, v2 = map(int, input().split())

case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

print(-1 if case1 >= 1e10 and case2 >= 1e10 else min(case1, case2))
