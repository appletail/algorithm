from collections import defaultdict

def solution(nums):
    ponket = defaultdict(int)
    for i in nums:
        ponket[i] += 1
        
    N = len(nums) // 2
    ponketCnt = len(ponket.keys())
    
    return N if ponketCnt > N else ponketCnt