def solution(numbers):
    numbers = list(map(str, sorted(numbers, key=lambda x: str(x) * 3, reverse=True)))
    return str(int(''.join(numbers)))