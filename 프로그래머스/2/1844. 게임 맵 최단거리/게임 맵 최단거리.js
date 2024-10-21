function solution(maps) {
    const n = maps.length
    const m = maps[0].length
    
    const visited = Array.from(Array(n), () => Array(m).fill(0))
    const q = [[0, 0]]
    visited[0][0] = 1
    while (q.length > 0) {
        const [r, c] = q.shift()
        if(r === n-1 && c === m-1) {
            return visited[r][c]
        }
        for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
            const nr = r + dr
            const nc = c + dc
            if (0 <= nr && nr < n && 0 <= nc && nc < m) {
                if (maps[nr][nc] === 1 && !visited[nr][nc]) {
                    visited[nr][nc] = visited[r][c] + 1
                    q.push([nr, nc])
                }
            }
        }
    }

    return -1;
}