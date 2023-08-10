import sys
from heapq import heappop, heappush


def dijk(graph, start):
    total_costs = [1e10] * (N + 1)
    total_costs[start] = 0
    queue = []
    heappush(queue, (start, total_costs[start]))
    while queue:
        node, cost = heappop(queue)

        if total_costs[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = total_costs[node] + next_cost
            if new_cost < total_costs[next_node]:
                total_costs[next_node] = new_cost
                heappush(queue, (next_node, new_cost))

    return total_costs


input = sys.stdin.readline
N = int(input())
M = int(input())

GRAPH = [[] for _ in range(N + 1)]
for _ in range(M):
    DEPART, ARRIVE, COST = map(int, input().split())
    GRAPH[DEPART].append([ARRIVE, COST])
START, END = map(int, input().split())

print(dijk(GRAPH, START)[END])
