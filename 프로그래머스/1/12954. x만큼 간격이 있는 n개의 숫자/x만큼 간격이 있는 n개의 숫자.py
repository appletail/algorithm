def solution(x, n):
    if x == 0:
        return [0] * n
    answer = [i for i in range(x, x*n+(1 if x >= 0 else -1), x)]
    
    return answer