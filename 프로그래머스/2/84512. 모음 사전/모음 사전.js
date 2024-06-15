let count = 0
let curWord = []

const findWord = (word, idx) => {
    if (curWord.join('') === word) return true
    if (idx == 5) return
    for (const vowels of ['A', 'E', 'I', 'O', 'U']) {
        count++
        curWord.push(vowels)
        isFind = findWord(word, idx+1)
        if (isFind) return true
        curWord.pop()
    }
    
    return false
}

function solution(word) {
    findWord(word, 0)
    return count
}