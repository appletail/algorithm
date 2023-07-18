class NodeQueue {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

class Queue {
    constructor() {
        this.front = null
        this.rear = null
        this.size = 0
    }
    
    isEmpty() {
        return !this.size
    }
    
    enqueue(data) {
        const node = new NodeQueue(data)
        if (this.isEmpty()) {this.front = node}
        else {this.rear.next = node}
        this.rear = node
        this.size++
    }
    
    dequeue() {
        if (this.isEmpty()) {return false}
        const value = this.front.data
        this.front = this.front.next
        this.size--
        if (this.isEmpty()) {this.rear = null}
        
        return value
    }
}

function solution(n, edge) {
    const graph = {}
    for (i of edge) {
        const [de, ar] = i
        if (graph[de]) {graph[de].push(ar)}
        else {graph[de] = [ar]}
        if (graph[ar]) {graph[ar].push(de)}
        else {graph[ar] = [de]}
    }
    
    const visited = Array.from(Array(n + 1), () => 0)
    visited[1] = 1
    const q = new Queue()
    q.enqueue(1)
    let answer = [0, 0]  // 최대거리, 갯수
    while (!q.isEmpty()) {
        const v = q.dequeue()
        if (visited[v] > answer[0]) {answer = [visited[v], 1]}
        else if (visited[v] === answer[0]) {answer[1]++}
        
        for (node of graph[v]) {
            if (!visited[node]) {
                q.enqueue(node)
                visited[node] = visited[v] + 1
            }
        }
    }

    return answer[1]
}