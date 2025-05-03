def solution(info, n, m):
    answer = 1000
    stack = [(-1, 0, 0)]
    used = set()
    used.add((-1, 0, 0))
    while stack:
        idx, A, B = stack.pop()
        if idx == len(info)-1:
            answer = min(answer, A)
        else:
            a, b = info[idx+1]
            newA = (idx+1, A+a, B)
            newB = (idx+1, A, B+b)
            if A + a < n and A + a < answer and newA not in used:
                stack.append(newA)
                used.add(newA)
            if B + b < m and newB not in used:
                stack.append(newB)
                used.add(newB)

    return answer if answer != 1000 else -1
