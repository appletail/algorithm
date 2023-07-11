function solution(s){
    const stack = []
    for (i of s) {
        if (i === '(') {
            stack.push(i)
            continue
        }
        if (stack.length === 0 || stack.pop() !== '(') return false
    }
    if (stack.length !== 0) return false 
    
    return true;
}