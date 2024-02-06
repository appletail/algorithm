import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b], G[b][a] = True, True

sumV = [0] * (N + 1)

for a in range(1, N + 1):
    q = deque([a])
    visited = [0] * (N + 1)
    while q:
        v = q.popleft()
        for b in range(1, N + 1):
            if G[v][b] and not visited[b]:
                visited[b] = visited[v] + 1
                q.append(b)

    sumV[a] = sum(visited) - visited[a]

minV = 1e10
answer = 0
for i in range(1, N + 1):
    if sumV[i] < minV:
        minV = sumV[i]
        answer = i

print(answer)
