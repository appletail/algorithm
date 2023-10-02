function solution(array, commands) {
    var answer = [];
    commands.forEach((command) => {
        const sliced = array.slice(command[0] - 1, command[1])
        sliced.sort((a, b) => a - b)
        answer.push(sliced[command[2] - 1])
    })
    return answer;
}