function solution(brown, yellow) {
    const answer = [];
    for (let row = 1; row <= yellow; row++) {
        if (yellow % row === 0) {
            const col = yellow / row
            if (row * 2 + col * 2 + 4 === brown) {
                answer.push(col + 2)
                answer.push(row + 2)
                break
            }
        }    
    }
    
    return answer;
}