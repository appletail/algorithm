from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    remain = deque()
    
    for idx in range(len(speeds)):
        remain.append(ceil((100 - progresses[idx]) / speeds[idx]))
    
    cnt, compare = 0, remain[0]
    while remain:
        num = remain.popleft()
        cnt += 1
        if num > compare:
            answer.append(cnt - 1)
            compare = num
            cnt = 1
    else:
        answer.append(cnt)    
        
    return answer