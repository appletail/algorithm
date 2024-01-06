from collections import deque

def solution(priorities, location):
    answer = 0
    count = [0] * 10
    queue = deque()
    for i in range(len(priorities)):
        count[priorities[i]] += 1
        queue.append((priorities[i], True) if location == i else (priorities[i], False))

    while queue:
        prior, flag = queue.popleft()
        for i in range(prior + 1, 10):
            if count[i]:
                queue.append((prior, flag))
                break
        else:
            answer += 1
            count[prior] -= 1
            if flag:
                break
    
    return answer