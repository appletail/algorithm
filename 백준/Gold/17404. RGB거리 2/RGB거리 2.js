const fs = require("fs")
const filePath = process.platform === "linux" ? "dev/stdin" : "백준/input.txt"
const input = fs.readFileSync(filePath).toString().split("\n")

const N = Number(input[0])
const houses = input.reduce((acc, v, i) => {
  if (i !== 0) acc.push(v.split(" ").map(Number))
  return acc
}, [])

let answer = Infinity
houses[0].forEach((first, idx) => {
  const dp = Array.from(new Array(N), () => new Array(3).fill(Infinity))
  dp[0].fill(first)
  for (let i = 0; i < N - 1; i++) {
    for (let j = 0; j < 3; j++) {
      ;[1, -1].forEach((v) => {
        const d = (j + v + 3) % 3
        if (i === N - 2 || i === 0) {
          if (d !== idx) {
            dp[i + 1][d] = Math.min(dp[i + 1][d], dp[i][j] + houses[i + 1][d])
          }
        } else
          dp[i + 1][d] = Math.min(dp[i + 1][d], dp[i][j] + houses[i + 1][d])
      })
    }
  }
  answer = Math.min(answer, ...dp[N - 1])
})

console.log(answer)
