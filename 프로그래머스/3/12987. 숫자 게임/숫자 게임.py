def solution(A, B):
    answer = 0
    sortedA = sorted(A)
    sortedB = sorted(B)

    bIdx = 0
    for num in sortedA:
        while bIdx < len(sortedB) and sortedB[bIdx] <= num:
            bIdx += 1

        if bIdx >= len(sortedB):
            break
        else:
            answer += 1

        bIdx += 1

    return answer