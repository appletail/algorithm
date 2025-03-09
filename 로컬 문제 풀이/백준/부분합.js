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


// 다른 답
const otherAnswer = () => {
  const fs = require("fs");
  const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  
  // 10000 이하의 자연수로 이루어진 n짜리 수열
  // 부분합 중 s 이상 되는 것 중 가장 짧은 길이
  const [n, s] = input[0].split(" ").map(Number);
  const arr = input[1].split(" ").map(Number);
  
  let minLength = Infinity;
  let sum = 0;
  let leftIdx = 0;
  
  for (let rightIdx = 0; rightIdx < n; rightIdx++) {
    sum += arr[rightIdx];
    while (sum >= s) {
      minLength = Math.min(minLength, rightIdx - leftIdx + 1);
      sum -= arr[leftIdx];
      leftIdx++;
    }
  }
  
  console.log(minLength === Infinity ? 0 : minLength); 
}

otherAnswer()