from sys import stdin
from heapq import heappop, heappush

def main():
    N, M = int(stdin.readline()), int(stdin.readline())
    links = [set() for _ in range(N+1)]
    for _ in range(M):
        fr, to, cost = map(int, stdin.readline().split())
        links[fr].add((to, cost))
    start_node, end_node = map(int, stdin.readline().split())
    q = [(0, start_node)]
    check = [[10**9, 0] for _ in range(N+1)]
    check[start_node][0] = 0
    while q:
        total_cost, node = heappop(q)
        if node == end_node:
            break
        for next_node, next_cost in links[node]:
            if total_cost+next_cost < check[next_node][0]:
                check[next_node][0], check[next_node][1] = total_cost+next_cost, node
                heappush(q, (total_cost+next_cost, next_node))
    route = [end_node]
    previous_node = check[end_node][1]
    while previous_node:
        route.append(previous_node)
        previous_node = check[previous_node][1]
    print(check[end_node][0], len(route))
    print(*route[::-1])

main()