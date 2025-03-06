let fs = require('fs');
filepath = process.platform === 'linux' ? 'dev/stdin' : '백준/input.txt' 
let input = fs.readFileSync(filepath).toString().trim().split('\n');

const findRoot = (idx) => {
  const temp = []
  while (idx != union[idx]) {
    temp.push(idx)
    idx = union[idx]
  }
  temp.forEach(v => {
    union[v] = idx
  })
  return idx
}

const [N, M] = input[0].split(' ').map(v => Number(v))
const nodes = []

for (let i=1; i < input.length; i++) {
  nodes.push(input[i].split(' ').map(v => Number(v)))
}

const union = Array.from(Array(N+1), (_, i) => i)
nodes.sort((a, b) => a[2] - b[2])

let cnt = 0
let answer = 0
for (let i=0; i<M; i++) {
  const [A, B, C] = nodes[i]
  const [rootA, rootB] = [findRoot(A), findRoot(B)]
  if (rootA !== rootB) {
    cnt += 1
    answer += C
    if (rootA > rootB) {
      union[rootA] = rootB
    } else {
      union[rootB] = rootA
    }
  }
  if (cnt === N-1) {
    answer -= C
    break
  }
}

console.log(answer)
