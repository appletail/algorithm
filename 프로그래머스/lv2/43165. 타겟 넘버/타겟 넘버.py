def findTargets(numbers, target, i, cSum, L, count):
    if i == L:
        if cSum == target:
            count += 1
        return count
    
    count = findTargets(numbers, target, i + 1, cSum + numbers[i], L, count)
    count = findTargets(numbers, target, i + 1, cSum - numbers[i], L, count)
    
    return count
    
def solution(numbers, target):
    L = len(numbers)
    answer = findTargets(numbers, target, 0, 0, L, 0)

    return answer