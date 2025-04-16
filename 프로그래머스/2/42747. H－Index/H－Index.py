def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for i in range(1, n+1):
        h = citations[-i]
        if h >= i:
            answer = i
        else:
            break

    return answer
