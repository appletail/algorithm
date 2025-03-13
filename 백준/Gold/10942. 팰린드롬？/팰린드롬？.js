const fs = require("fs")
const filePath = process.platform === "linux" ? "dev/stdin" : "백준/input.txt"
const input = fs.readFileSync(filePath).toString().split("\n")

const N = Number(input[0])
const nums = input[1].split(" ").map(Number)
const M = Number(input[2])

const dp = Array.from(Array(N), () => new Array(N).fill(0))

for (let i = 0; i < N; i++) {
  dp[i][i] = 1
}

for (let j = 0; j < N; j++) {
  for (let i = 0; i < j; i++) {
    let [S, E] = [i, j]
    if (nums[S] !== nums[E]) {
      continue
    }
    S += 1
    E -= 1
    if (S > E || dp[S][E]) dp[i][j] = 1
  }
}

let answer = []
for (let i = 3; i < M + 3; i++) {
  const [S, E] = input[i].split(" ").map(Number)
  answer.push(dp[S - 1][E - 1])
}
console.log(answer.join("\n"))
