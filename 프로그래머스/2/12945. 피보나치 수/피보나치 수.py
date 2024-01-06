def solution(n):
    first, second = 0, 1
    for _ in range(n - 1):
        first, second = second, first + second

    return second % 1_234_567