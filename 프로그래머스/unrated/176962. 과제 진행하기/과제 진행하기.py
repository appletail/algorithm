def solution(plans):
    answer = []
    incomplete = []
    for i in plans:
        hour, minute = list(map(int, i[1].split(':')))
        i[1] = minute + hour * 60

    plans = sorted(plans, key= lambda x: x[1])
    
    for i in range(1, len(plans)):
        remain_time = plans[i][1] - plans[i - 1][1] - int(plans[i - 1][2])
        
        if remain_time >= 0:
            answer.append(plans[i - 1][0])
            while incomplete and remain_time > 0:
                remain_time_copy = remain_time - incomplete[-1][2]
                incomplete[-1][2] -= remain_time
                remain_time = remain_time_copy
                if incomplete[-1][2] <= 0:
                    answer.append(incomplete.pop()[0])
        else:
            plans[i - 1][2] = -remain_time
            incomplete.append(plans[i - 1])
    else:
        answer.append(plans[-1][0])
    
    answer += [i[0] for i in incomplete][::-1]
    
    return answer