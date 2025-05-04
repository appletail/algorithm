def solution(s):
    p, y = 0, 0
    for cha in s:
        if cha.lower() == 'p':
            p += 1
        elif cha.lower() == 'y':
            y += 1
    return True if p == y else False