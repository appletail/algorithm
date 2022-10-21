let tmp = 4
for (i = 1; i < 10; i+=2) {
  let star = ''

  for (j = 0; j < tmp; j++) {
    star += ' '
  }
  
  for (k = 0; k < i; k++) {
    star += '*'
  }

  tmp -= 1
  console.log(star)
}
