const scissorsButton = document.getElementById('scissors-button')
const rockButton = document.getElementById('rock-button')
const paperButton = document.getElementById('paper-button')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')

modal.addEventListener('click', event => {
  modal.style.display = 'none'
})

let count1 = 0
let count2 = 0

const playGame = (player1, player2) => {
  if (player1 === 'scissors') {
    if (player2 === 'rock') {
      count2 += 1
      return 2
    } else if (player2 === 'paper') {
      count1 += 1
      return 1
    } 
  } else if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1 += 1
      return 1
    } else if (player2 === 'paper') {
      count2 += 1
      return 2
    }
  } else {
    if (player2 === 'rock') {
      count1 += 1
      return 1
    } else if (player2 === 'scissors') {
      count2 += 1
      return 2
    }
  }
  return 0
}


const buttonClickHandler = choice => event => {
  scissorsButton.disabled = true
  rockButton.disabled = true
  paperButton.disabled = true

  const cases = ['scissors', 'rock', 'paper']
  const randomIndex = Math.floor(Math.random() * 3)
  
  const result = playGame(choice, cases[randomIndex])

  const player1Img = document.querySelector('#player1-img')
  const player2Img = document.querySelector('#player2-img')

  player1Img.src = `./img/${choice}.png`

  let i = randomIndex + 1
  const rotateImg = () => {
    i = (i + 1) % 3
    player2Img.src = `./img/${cases[i]}.png`
  }
  const timerId = setInterval(rotateImg, 100)
  setTimeout(() => {
    clearInterval(timerId)
    const countA = document.querySelector('.countA')
    const countB = document.querySelector('.countB')
    countA.innerText = count1
    countB.innerText = count2
    player2Img.src = `./img/${cases[randomIndex]}.png`
    modalContent.innerText = result ? `player${result} 의 승리입니다!` : '무승부입니다!'
    modal.style.display = 'flex'
    scissorsButton.disabled = false
    rockButton.disabled = false
    paperButton.disabled = false
  }, 3000)
}

scissorsButton.addEventListener('click', buttonClickHandler('scissors'))
rockButton.addEventListener('click', buttonClickHandler('rock'))
paperButton.addEventListener('click', buttonClickHandler('paper'))