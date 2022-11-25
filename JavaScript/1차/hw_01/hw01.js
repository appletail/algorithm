// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.
// for 구문안의 i는 하나씩 숫자가 1씩 오를때마다 재할당되면서 사용되는데 const는 재할당이 불가능하여 오류가 발생합니다. const를 let으로 수정합니다.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
// for in 구문은 객체에 사용하는 것으로 위 코드는 객체의 key값을 출력하고 있습니다. for of 구문으로 수정해야합니다.