def solution(my_strings, parts):
    answer = ''
    for idx, ms in enumerate(my_strings):
        answer += ms[parts[idx][0]:parts[idx][1]+1]
    return answer