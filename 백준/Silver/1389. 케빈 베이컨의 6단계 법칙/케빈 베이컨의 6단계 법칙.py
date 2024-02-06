import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b], G[b][a] = 1, 1

minV = 1e10
answer = 0
sumV = [0] * (N + 1)
for a in range(1, N + 1):
    q = deque([a])
    visited = [0] * (N + 1)
    visited[a] = 1
    while q:
        v = q.popleft()
        for b in range(1, N + 1):
            if G[v][b] and not visited[b]:
                visited[b] = visited[v] + 1
                q.append(b)

    sumV[a] = sum(visited)
    if sumV[a] < minV:
        minV = sumV[a]
        answer = a

print(answer)
