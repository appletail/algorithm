def solution(answers):
    answer = []
    count = [0, 0, 0, 0]
    dumb1 = [1, 2, 3, 4, 5]
    dumb2 = [2, 1, 2, 3, 2, 4, 2, 5]
    dumb3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, value in enumerate(answers):
        if dumb1[idx % len(dumb1)] == value:
            count[1] += 1
        if dumb2[idx % len(dumb2)] == value:
            count[2] += 1
        if dumb3[idx % len(dumb3)] == value:
            count[3] += 1
            
    maxV = 0
    for i in range(1, len(count)):
        if count[i] > maxV:
            answer = [i]
            maxV = count[i]
        elif count[i] == maxV:
            answer.append(i)
        
    return answer