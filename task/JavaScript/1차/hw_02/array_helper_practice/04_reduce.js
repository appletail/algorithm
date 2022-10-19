// 1. 배열에 담긴 중복된 이름을 {'이름': 수} 형태의 object로 반환하세요.

const names = ['harry', 'aiden', 'julie', 'julie', 'edward']

// answer
console.log(names.reduce((acc, cur) => {
  if (acc[cur] === undefined) {
    acc[cur] = 1
  } else {
    acc[cur] += 1
  }
  return acc
}, {}))


console.log(names.reduce((acc, cur) => {
  acc[cur] = (acc[cur] || 0) + 1
  return acc
}, {}))