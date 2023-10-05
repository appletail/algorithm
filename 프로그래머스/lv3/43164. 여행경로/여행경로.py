airRoute = []
def dfs(tickets, used, i, s, answer, L):
    global airRoute
    
    if airRoute:
        return

    if i == L:
        airRoute = answer
        return

    depart = s.pop()
    
    for idx in range(L):
        d, a = tickets[idx]
        if not used[idx] and depart == d:
            s.append(a)
            answer.append(a)
            used[idx] = 1
            dfs(tickets, used, i + 1, s, answer, L)
            if airRoute:
                break
            answer.pop()
            used[idx] = 0
    
        

def solution(tickets):
    global airRoute
    
    answer = ["ICN"]
    L = len(tickets)
    used = [0] * (L + 1)
    used[-1] = 1
    tickets = sorted(tickets)
    dfs(tickets, used, 0, ["ICN"], answer, L)
    
    return airRoute