from itertools import combinations

def checkNum(comb, check, m, ans):
    for idx in range(m):
        cnt = 0
        for num in comb:
            if check[idx][num]:
                cnt += 1
        if cnt != ans[idx]:
            return False
    return True


def solution(n, q, ans):
    answer = 0
    m = len(q)
    check = [[0] * (n+1) for _ in range(m)]
    for i in range(m):
        for num in q[i]:
            check[i][num] = 1
    nums = [i for i in range(1, n+1)]
    
    max_ans_idx = ans.index(max(ans))
    for comb in combinations(nums, 5):
        if checkNum(comb, check, m, ans):
            answer += 1
            
    return answer
