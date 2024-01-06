function solution(sizes) {
    const [long, short] = [[], []]
    for ([garo, sero] of sizes) {
        if (garo >= sero) {
            long.push(garo)
            short.push(sero)
        } else {
            long.push(sero)
            short.push(garo)
        }
    }
    return Math.max(...long) * Math.max(...short)
}