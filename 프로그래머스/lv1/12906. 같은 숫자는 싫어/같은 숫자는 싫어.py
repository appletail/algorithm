def solution(arr):
    answer = [-1]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
            
    return answer[1:]