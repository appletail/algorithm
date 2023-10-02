function solution(n, lost, reserve) {
    let answer = n - lost.length;
    const lostCheck = Array(n + 1).fill(0)
    reserve.sort((a, b) => a - b)
    lost.forEach((e) => {
        const isReserve = reserve.indexOf(e)
        if (isReserve == -1) lostCheck[e] = 1
        else {
            reserve.splice(isReserve, 1)
            answer += 1
        }
    })

    reserve.forEach((e) => {
        if (e - 1 !== 0 && lostCheck[e - 1]) {
            lostCheck[e - 1] = 0
            answer += 1
        } else if (e + 1 !== n + 1 && lostCheck[e + 1]) {
            lostCheck[e + 1] = 0
            answer += 1
        }
    })
    
    return answer;
}