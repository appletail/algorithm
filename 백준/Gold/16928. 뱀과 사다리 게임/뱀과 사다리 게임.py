import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited = [-1] * 110
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        v = q.popleft()
        if v >= 100:
            return visited[v]
        else:
            for i in graph[v]:
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[v] + 1


n, m = map(int, input().split())
graph = [[i + 1, i + 2, i + 3, i + 4, i + 5, i + 6] for i in range(101)]
for _ in range(n + m):
    x, y = map(int, input().split())
    graph[x] = [y + 1, y + 2, y + 3, y + 4, y + 5, y + 6]

print(bfs())
