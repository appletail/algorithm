# import heapq

# def solution(jobs):
#     answer = 0
#     length = len(jobs)
#     jobs = [[spend, start] for start, spend in jobs]
#     heapq.heapify(jobs)
    
#     time = 0
#     while jobs:
#         tmps = []
        
#         while jobs:
#             spend, start = heapq.heappop(jobs)
#             if start > time:
#                 tmps.append([spend, start])
#             else:
#                 break

#         if start <= time:
#             answer += time - start + spend
#             time += spend
#         else:
#             time += 1
            
#         while tmps:
#             tmp = tmps.pop()
#             heapq.heappush(jobs, tmp)
    
#     return answer // length

# 다른 답
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)