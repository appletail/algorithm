import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    jobs = [[spend, start] for start, spend in jobs]
    heapq.heapify(jobs)
    
    time = 0
    while jobs:
        tmps = []
        
        while jobs:
            spend, start = heapq.heappop(jobs)
            if start > time:
                tmps.append([spend, start])
            else:
                break

        if start <= time:
            answer += time - start + spend
            time += spend
        else:
            time += 1
            
        while tmps:
            tmp = tmps.pop()
            heapq.heappush(jobs, tmp)
    
    return answer // length