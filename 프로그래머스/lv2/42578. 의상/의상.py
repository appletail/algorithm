from collections import defaultdict

def solution(clothes):
    answer = 1
    apperals = defaultdict(int)
    for apperal, apperal_type in clothes:
        apperals[apperal_type] += 1
    
    clothes_cnt = list(apperals.values())
    
    for i in clothes_cnt:
        answer *= i + 1
    
    return answer - 1