import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    answer = 'NO'
    N, M, W = map(int, input().split())
    roads = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        roads.append([S, E, T])
        roads.append([E, S, T])
    for _ in range(W):
        S, E, T = map(int, input().split())
        roads.append([S, E, -T])

    INF = 1e10
    distance = [INF] * (N + 1)
    distance[1] = 0
    for V in range(N):
        for road in roads:
            S, E, T = road
            if (newRoute := distance[S] + T) < distance[E]:
                distance[E] = newRoute
                if V == N - 1:
                    answer = 'YES'

    print(answer)
    