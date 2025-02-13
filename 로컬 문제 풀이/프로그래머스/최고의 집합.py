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


test = [
    [[1, 1, 1, 1], [1, 1, 1, 1], 0],
    [[5, 1, 3, 7], [2, 2, 6, 8], 3],
    [[2, 2, 2, 2], [1, 1, 1, 1], 0],
]

for tc, value in enumerate(test):
    print('TC:', tc + 1)
    A, B, result = value
    answer = solution(A, B)
    print('====================================')
    print('pass' if answer == result else 'fail')
    print('====================================')
    print()
