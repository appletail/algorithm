import sys
input = sys.stdin.readline
from collections import deque

def chicken_distance(n, s, cd):
    if n == M:
        house_cnt = 0
        distances = 0
        visited = [[-1] * N for _ in range(N)]
        for sr, sc in selected:
            visited[sr][sc] = 0
        q = deque(selected)
        while q:
            r, c = q.popleft()
            if city[r][c] == 1:
                house_cnt += 1
                distances += visited[r][c]
                if distances >= cd:
                    return cd
                if house_cnt == number_of_houses:
                    break
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append([nr, nc])

        return distances
    else:
        for idx in range(s, len(chicken_restaurants)):
            selected.append(chicken_restaurants[idx])
            cd = chicken_distance(n+1, idx+1, cd)
            selected.pop()
        return cd

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

number_of_houses = 0
chicken_restaurants = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            number_of_houses += 1
        elif city[i][j] == 2:
            chicken_restaurants.append([i, j])

selected = []
print(chicken_distance(0, 0, 1e10))
