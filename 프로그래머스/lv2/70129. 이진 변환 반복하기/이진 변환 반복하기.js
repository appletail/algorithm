function solution(s) {
    let binary = s
    let transCnt = 0
    let zeroCnt = 0

    while (binary !== "1") {
        const [value, cnt] = deleteZero(binary)
        binary = value
        zeroCnt += cnt
        binary = binaryTrans(binary)
        transCnt += 1
    }
    return [transCnt, zeroCnt];
}

function deleteZero(num) {
    let cnt = 0
    let value = ""
    for (let i = 0; i < num.length; i++) {
        if (num[i] == "1") value += "1"
        else cnt += 1
    }
    return [value, cnt]
}

function binaryTrans(num) {
    let value = 0
    let c = num.length
    let digit = 1
    while (c !== 1) {
        value += (c % 2) * digit
        c = parseInt(c / 2)
        digit *= 10
    }
    value += digit
    return value.toString()
}