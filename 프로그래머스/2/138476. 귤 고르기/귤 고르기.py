from collections import defaultdict

def solution(k, tangerine):
    tang = defaultdict(int)
    
    for i in range(len(tangerine)):
        tang[tangerine[i]] += 1
    tang = sorted(tang.values(), reverse=True)
    
    cnt = 0
    for i in range(len(tang)):
        cnt += tang[i]
        if cnt >= k:
            return i + 1

