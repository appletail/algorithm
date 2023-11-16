def solution(n):
    answer = 0

    first, second = 0, 1
    for _ in range(n - 1):
        answer = first + second
        first, second = second, answer

    return answer % 1_234_567