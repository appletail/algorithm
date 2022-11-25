function palindrome1(str) {
  let tmp = ''
  for (let index = 1; index < str.length + 1; index++) {
    tmp += str[str.length - index]
  }
  if (str == tmp) {
    console.log(true)
  } else {
    console.log(false)
  }
}

// 출력
palindrome1('level') // => true
palindrome1('hi') // => false


function palindrome2(str) {
  for (let idx = 0; idx < str.length; idx++) {
    let left = str[idx]
    let right = str[str.length - idx - 1]
    if (left != right) {
      console.log(false)
      return
    }
}
console.log(true)
}



// 출력
palindrome2('level') // => true
palindrome2('hi') // => false

