# airRoute = []
# def dfs(tickets, used, i, s, answer, L):
#     global airRoute
    
#     if airRoute:
#         return

#     if i == L:
#         airRoute = answer
#         return

#     depart = s.pop()
    
#     for idx in range(L):
#         d, a = tickets[idx]
#         if not used[idx] and depart == d:
#             s.append(a)
#             answer.append(a)
#             used[idx] = 1
#             dfs(tickets, used, i + 1, s, answer, L)
#             if airRoute:
#                 break
#             answer.pop()
#             used[idx] = 0
    
        

# def solution(tickets):
#     global airRoute
    
#     answer = ["ICN"]
#     L = len(tickets)
#     used = [0] * (L + 1)
#     used[-1] = 1
#     tickets = sorted(tickets)
#     dfs(tickets, used, 0, ["ICN"], answer, L)
    
#     return airRoute

from collections import defaultdict


def dfs(graph, n, depart, route):
    if len(route) == n + 1:
        return route
    
    for idx, arrive in enumerate(graph[depart]):
        graph[depart].pop(idx)
        route.append(arrive)
        answer = dfs(graph, n, arrive, route)
        
        if answer: 
            return answer
        
        route.pop()
        graph[depart].insert(idx, arrive)
        

def solution(tickets):
    graph = defaultdict(list)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for value in graph.values():
        value.sort()

    answer = dfs(graph, len(tickets), 'ICN', ['ICN'])

    return answer
