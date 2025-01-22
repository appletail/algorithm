from collections import deque

def hideAndSeek(cur, dest):
    visited = [[0, 0] for _ in range(100001)]
    q = deque()
    visited[cur][1] = 1
    q.append(cur)
    while q:
        v = q.popleft()
        if v == dest:
            return visited[v]

        for dv in [(v+1), (v-1), (v*2)]:
            if 0 <= dv <= 100_000:
                if not visited[dv][1]:
                    visited[dv][0] = visited[v][0] + 1
                    visited[dv][1] = visited[v][1]
                    q.append(dv)
                elif visited[dv][0] == visited[v][0] + 1:
                    visited[dv][1] += visited[v][1]


N, K = map(int, input().split())
for answer in hideAndSeek(N, K):
    print(answer)
