def solution(schedules, timelogs, startday):
    member_len = len(timelogs)
    answer = 0
    for i in range(member_len):
        schedule = schedules[i] + 10
        if (schedule % 100) - 59 > 0:
            schedule += 100 - 60
        day = startday
        for timelog in timelogs[i]:
            if day != 6 and day != 7 and timelog > schedule:
                break
            day = day + 1 if day + 1 < 8 else 1
        else:
            answer += 1

    return answer
