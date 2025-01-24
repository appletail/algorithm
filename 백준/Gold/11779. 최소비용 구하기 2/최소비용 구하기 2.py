import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

depart, arrive = map(int, input().split())

INF = 1e10
distance = [[INF, ''] for _ in range(n + 1)]
q = []
heapq.heappush(q, (0, depart, f'{depart}'))
distance[depart] = [0, f'{depart}']
while q:
    dist, s, route = heapq.heappop(q)
    if distance[s][0] < dist:
        continue

    for e, w in graph[s]:
        if dist + w < distance[e][0]:
            distance[e] = [dist + w, f'{route},{e}']
            heapq.heappush(q, (dist + w, e, f'{route},{e}'))

print(distance[arrive][0])
route = distance[arrive][1].split(',')
print(len(route))
print(*route)
