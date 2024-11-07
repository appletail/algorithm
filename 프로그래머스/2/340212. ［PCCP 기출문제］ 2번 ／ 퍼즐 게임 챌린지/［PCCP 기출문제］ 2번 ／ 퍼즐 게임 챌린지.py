def is_possible(level, diffs, times, limit):
    n = len(diffs)
    time_passed, time_prev = 0, 0
    
    for idx in range(n):
        if diffs[idx] > level:
            time_passed += (time_prev+times[idx]) * (diffs[idx]-level)
        time_passed += times[idx]
        if time_passed > limit:
            return False
        time_prev = times[idx]
    
    return True
    
def solution(diffs, times, limit):
    answer = 0
    level_min, level_max = min(diffs), max(diffs)
    
    while level_min <= level_max:
        level_cur = (level_max+level_min) // 2
        possible = is_possible(level_cur, diffs, times, limit)

        if possible:
            answer = level_cur
            level_max = level_cur - 1
        else:
            level_min = level_cur + 1


    return answer
