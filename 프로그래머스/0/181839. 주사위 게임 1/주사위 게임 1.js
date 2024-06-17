const isOdd = (num) => {
    if (num % 2 == 0) return false
    return true
}

function solution(a, b) {
    const isAOdd = isOdd(a)
    const isBOdd = isOdd(b)
    
    return isAOdd && isBOdd ? a ** 2 + b ** 2 : isAOdd || isBOdd ? 2 * (a + b) : Math.abs(a - b)
}