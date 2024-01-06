def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = len(citations)
    if citations[-1] >= n:
        return n
    
    for i in range(n - 1):
        h = i + 1
        if citations[i] >= h and citations[i + 1] <= h:
            answer = h
            break

    return answer