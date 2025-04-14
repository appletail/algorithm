def solution(n):
    answer = 0
    cnt = 1
    
    while cnt <= n:
        answer += 1
        while '3' in str(answer) or answer % 3 == 0:
            answer += 1
        cnt += 1
        
    return answer