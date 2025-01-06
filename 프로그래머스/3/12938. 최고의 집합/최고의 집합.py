def solution(n, s):
    quotient = s // n
    remainder = s % n
    if quotient == 0:
        return [-1]

    answer = [quotient] * n
    for i in range(remainder):
        idx = i % n
        answer[idx] += 1

    answer.sort()
    return answer