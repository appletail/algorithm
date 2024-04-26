import sys
input = sys.stdin.readline
import heapq

def dijkstra(s):
    distance = [1e10] * (N + 1)
    distance[s] = 0

    heap = []
    heapq.heappush(heap, [distance[s], s])

    while heap:
        curDist, curNode = heapq.heappop(heap)

        if distance[curNode] < curDist:
            continue

        for nodeTo, dist in graph[curNode]:
            if distance[nodeTo] > (newDist:=curDist+dist):
                distance[nodeTo] = newDist
                heapq.heappush(heap, [newDist, nodeTo])

    return distance

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    r, c, d = map(int, input().split())
    graph[r].append([c, d])
    graph[c].append([r, d])
v1, v2 = map(int, input().split())

dijk1 = dijkstra(v1)
dijk2 = dijkstra(v2)

case1 = dijk1[1] + dijk1[v2] + dijk2[N]
case2 = dijk2[1] + dijk2[v1] + dijk1[N]

print(-1 if case1 >= 1e10 and case2 >= 1e10 else min(case1, case2))
