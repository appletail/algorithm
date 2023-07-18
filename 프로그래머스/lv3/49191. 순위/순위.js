function solution(n, results) {
    let answer = 0;
    const graph = new Array(n + 1).fill(0).map(() => Array(n + 1).fill(false))
    for (const match of results) {
        const [A, B] = match
        graph[A][B] = 1
        graph[B][A] = -1
        graph[A][A] = 0
        graph[B][B] = 0
    }
    const rangeN = [...new Array(n + 1).keys()]
    
    for (const A in rangeN) {
        for (const mid in rangeN) {
            for (const B in rangeN) {
                if (graph[A][mid] === 1 && graph[mid][B] === 1) {
                    graph[A][B] = 1
                    graph[B][A] = -1
                } else if (graph[B][mid] === 1 && graph[mid][A] === 1) {
                    graph[B][A] = 1
                    graph[A][B] = -1
                }
            }
        }
    }
    
    for (const i of graph) {
        let falseCnt = 0
        for (const j of i) {
            if (j === false) falseCnt++
            if (falseCnt === 2) break
        }
        if (falseCnt === 1) answer++
    }
    
    
    return answer;
}