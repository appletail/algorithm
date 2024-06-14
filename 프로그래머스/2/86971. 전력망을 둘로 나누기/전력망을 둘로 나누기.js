const countV = (start, tree, ignore) => {
    const visited = Array(tree.length).fill(false)
    let count = 1
    const stack = [start]
    visited[start] = true
    
    while (stack.length !== 0) {
        const v1 = stack.pop()
        for (const v2 of tree[v1]) {
            if (v2 === ignore) continue
            if (!visited[v2]) {
                stack.push(v2)
                visited[v2] = true
                count++
            }
        }
    }
    
    return count
    
}

function solution(n, wires) {
    let answer = 100;
    const tree = Array.from(Array(n + 1), () => Array())
    for (const idx in wires) {
        const [ v1, v2 ] = wires[idx]
        tree[v1].push(v2)
        tree[v2].push(v1)
    }

    for (const idx in wires) {
        const [ v1, v2 ] = wires[idx]
        
        const v1Count = countV(v1, tree, v2)
        const v2Count = countV(v2, tree, v1)
        const difference = Math.abs(v1Count - v2Count)

        answer = Math.min(answer, difference)
    }
    return answer;
}