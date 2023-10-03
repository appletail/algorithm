from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K and len(scoville) >= 2:
        food1 = heappop(scoville) 
        food2 = heappop(scoville)
        heappush(scoville, food1 + food2 * 2)
        answer += 1
        
    if not scoville or scoville[0] < K:
        answer = -1
    
    return answer