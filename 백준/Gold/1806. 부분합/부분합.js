const fs = require('fs')
const filePath = process.platform === 'linux' ? 'dev/stdin' : '백준/input.txt'
const input = fs.readFileSync(filePath).toString().trim().split('\n')

const [N, S] = input[0].split(' ').map(Number)
const nums = input[1].split(' ').map(Number)

let [left, right] = [-1, 0]
let curSum = nums[right]
let answer = Infinity

while (right < nums.length) {
  if (curSum >= S) {
    answer = Math.min(answer, right-left)
  }

  if (left+1 === right || curSum < S) {
    right += 1
    if (right < nums.length) {
      curSum += nums[right]
    }
  } else if (curSum >= S) {
    left += 1
    if (left < right)
      curSum -= nums[left]
  }
}

console.log(answer === Infinity ? 0 : answer)
