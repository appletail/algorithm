import heapq, sys
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([v, w])
d = [1e9 for _ in range(V + 1)]
d[K] = 0
pq = [(0, K)]

while pq:
    w, node = heapq.heappop(pq)
    if d[node] >= w:
        for next_node, next_w in edge[node]:
            new_w = d[node] + next_w
            if new_w < d[next_node]:
                d[next_node] = new_w
                heapq.heappush(pq, (new_w, next_node))

for i in range(1, V + 1):
    print(d[i] if d[i] != 1e9 else "INF")
