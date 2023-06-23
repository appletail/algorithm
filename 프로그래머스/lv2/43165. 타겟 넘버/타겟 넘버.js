function findTargets(numbers, target, i, cSum, L, count) {
    if (i === L) {
        if (cSum === target) {
            count += 1
        }
        return count
    }
    
    count = findTargets(numbers, target, i + 1, cSum + numbers[i], L, count)
    count = findTargets(numbers, target, i + 1, cSum - numbers[i], L, count)
    
    return count
}

function solution(numbers, target) {
    const L = numbers.length
    return findTargets(numbers, target, 0, 0, L, 0)
}
