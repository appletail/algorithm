def solution(array, commands):
    answer = []
    for command in commands:
        sliced = sorted(array[command[0] - 1: command[1]])
        answer.append(sliced[command[2] - 1])
    return answer