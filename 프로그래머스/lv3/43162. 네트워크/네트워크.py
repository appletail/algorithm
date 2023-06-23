def solution(n, computers):
    answer = 0
    visited = [0] * n
    for r in range(n):
        if visited[r]:
            continue
        
        answer += 1
        visited[r] = 1
        s = [r]
        while s:
            node = s.pop()
            for c in range(n):
                if computers[node][c] and not visited[c]:
                    visited[c] = 1
                    s.append(c)

    return answer
