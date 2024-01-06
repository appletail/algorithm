function solution(s){
    const stack = []
    for (const i of s) {
        if (i === '(') {
            stack.push(i)
            continue
        }
        if (stack.length === 0 || stack.pop() !== '(') return false
    }
    if (stack.length) return false   
    
    return true;
}