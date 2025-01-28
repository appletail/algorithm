import sys
input = sys.stdin.readline
import heapq

def dijk(start):
    INF = 1e10
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        s, acc = heapq.heappop(q)
        if acc > distance[s] or acc > m:
            continue
        for e, w in graph[s]:
            if acc + w < distance[e]:
                heapq.heappush(q, (e, acc+w))
                distance[e] = acc + w

    return distance

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])

answer = 0
for start in range(1, n+1):
    dists = dijk(start)
    curSum = 0
    for i in range(1, n+1):
        if dists[i] <= m:
            curSum += t[i]
    answer = max(answer, curSum)

print(answer)
