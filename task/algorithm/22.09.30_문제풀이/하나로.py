import sys
sys.stdin = open("input.txt", "r")

# 제출한 답(가장 빠름)
def prim():
    MST = [0] * N
    key = [1e100000] * N
    key[0] = 0

    for _ in range(N - 1):
        u = 0
        minV = 1e100000
        for i in range(N):
            if not MST[i] and key[i] < minV:
                u, minV = i, key[i]
        MST[u] = 1
        for v in range(N):
            if not MST[v] and GM[u][v] > 0:
                key[v] = min(key[v], GM[u][v])

    return sum(key)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    GM = [[0] * N for _ in range(N)]
    island = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    for i in range(N - 1):
        x, y = island[0][i], island[1][i]
        for j in range(i + 1, N):
            dx, dy = island[0][j], island[1][j]
            w = 0
            if x == dx:
                w = E * abs(y - dy) ** 2
            elif y == dy:
                w = E * abs(x - dx) ** 2
            else:
                w = E * (abs(x - dx) ** 2 + abs(y - dy) ** 2)
            GM[i][j] = w
            GM[j][i] = w
    print(f'#{test_case}', round(prim()))


# 다른 풀이(가장 느림)
def prim():
    MST = [0] * N
    MST[0] = 1
    s = 0
    for _ in range(N - 1):
        u = 0
        minV = 1e100000
        for i in range(N):
            if MST[i]:
                for j in range(N):
                    if not MST[j] and 0 < GM[i][j] < minV:
                        u = j
                        minV = GM[i][j]
        s += minV
        MST[u] = 1

    return s


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    GM = [[0] * N for _ in range(N)]
    island = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    for i in range(N - 1):
        x, y = island[0][i], island[1][i]
        for j in range(i + 1, N):
            dx, dy = island[0][j], island[1][j]
            w = 0
            if x == dx:
                w = E * abs(y - dy) ** 2
            elif y == dy:
                w = E * abs(x - dx) ** 2
            else:
                w = E * (abs(x - dx) ** 2 + abs(y - dy) ** 2)
            GM[i][j] = w
            GM[j][i] = w

    print(f'#{test_case}', round(prim()))


# 다른 답(두 번째로 빠름)
def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    GM = [[0] * N for _ in range(N)]
    island = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    edge = []
    for i in range(N - 1):
        x, y = island[0][i], island[1][i]
        for j in range(i + 1, N):
            dx, dy = island[0][j], island[1][j]
            w = 0
            if x == dx:
                w = E * abs(y - dy) ** 2
            elif y == dy:
                w = E * abs(x - dx) ** 2
            else:
                w = E * (abs(x - dx) ** 2 + abs(y - dy) ** 2)
            edge.append([i, j, w])
    edge.sort(key=lambda x: x[2])
    rep = [i for i in range(N)]

    cnt = 0
    total = 0
    for u, v, w in edge:
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            total += w
            if cnt == N - 1:
                break

    print(f'#{test_case}', round(total))


# 가장 빠른 답
def select_vertex(n, visited, dist, INF):
    vertex = -1
    min_dist = INF

    for i in range(n):
        if not visited[i] and min_dist > dist[i]:
            min_dist = dist[i]
            vertex = i

    return vertex, min_dist


def get_length(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def prim(N, x_lst, y_lst):
    INF = get_length(0, 0, 1000001, 1000001)
    visited = [False] * N
    dist = [INF] * N
    dist[0] = 0
    answer = 0.0

    for _ in range(N):
        U, minV = select_vertex(N, visited, dist, INF)

        if U == -1:
            break

        answer += minV
        visited[U] = True

        for v in range(N):
            if U != v and not visited[v]:
                dist[v] = min(dist[v], get_length(x_lst[U], y_lst[U], x_lst[v], y_lst[v]))

    return answer


tc = int(input())

for t in range(1, tc + 1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())

    answer = int(round(prim(N, x_lst, y_lst) * E))
    print(f'#{t} {answer}')