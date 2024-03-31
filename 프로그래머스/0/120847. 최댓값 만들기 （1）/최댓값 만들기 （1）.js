function solution(numbers) {
    const newNums = numbers.sort((a, b) => a - b)
    return newNums[newNums.length - 1] * newNums[newNums.length - 2];
}