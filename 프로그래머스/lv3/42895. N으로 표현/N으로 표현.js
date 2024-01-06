function solution(N, number) {
    const memo = new Array(9).fill(0).map(() => new Set())
    if (N == number) return 1
    memo.forEach((elem, idx) => elem.add(Number(String(N).repeat(idx))))
    
    for (let i = 1; i < 9; i++) {
        for (let j = 1; j < i; j++) {
            for (let A of memo[j]) {
                for (let B of memo[i - j]) {
                    memo[i].add(A + B)
                    memo[i].add(A - B)
                    memo[i].add(A * B) 
                    memo[i].add(A / B)
                }
            }
        }
        if (memo[i].has(number)) return i
    }
    return -1
}