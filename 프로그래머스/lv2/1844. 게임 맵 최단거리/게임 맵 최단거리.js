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
        if (this.size === 0) {this.front = node}
        else {this.rear.next = node}
        this.rear = node
        this.size++
    }
    dequeue() {
        if (this.size === 0) {return false}
        const value = this.front.data
        this.front = this.front.next
        this.size--
        if (this.size === 0) {this.rear = null}
        return value
    }
}


function bfs(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const visited = Array.from(Array(n), () => Array(m).fill(0))
    const dt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    const q = new Queue()
    q.enqueue([0, 0])
    
    while (!q.isEmpty()) {
        const v = q.dequeue()
        if (v[0] === n - 1 && v[1] === m -1) {
            return visited[v[0]][v[1]] + 1
        }
        for (const i of dt) {
            const nr = v[0] + i[0]
            const nc = v[1] + i[1]
            if (0 <= nr && nr < n && 0 <= nc && nc < m) {
                if (!visited[nr][nc] && !!maps[nr][nc]) {
                    visited[nr][nc] = visited[v[0]][v[1]] + 1
                    q.enqueue([nr, nc])
                }
            }
        }        
    }
    return -1
}

function solution(maps) {
    return bfs(maps);
}