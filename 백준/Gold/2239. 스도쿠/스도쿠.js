const fs = require("fs")
const filePath = process.platform === "linux" ? "dev/stdin" : "백준/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")

const sudoku = input.map((v) => v.trim().split("").map(Number))

const rows = Array.from(new Array(9), () => new Array(10).fill(0))
const columns = Array.from(new Array(9), () => new Array(10).fill(0))
const squares = Array.from(new Array(9), () => new Array(10).fill(0))
const blanks = []

const findSquareIdx = (i, j) => {
  return Math.floor(i / 3) * 3 + Math.floor(j / 3)
}

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (sudoku[i][j] === 0) blanks.push([i, j])
    else {
      rows[i][sudoku[i][j]] = 1
      columns[j][sudoku[i][j]] = 1
      squares[findSquareIdx(i, j)][sudoku[i][j]] = 1
    }
  }
}

const solve = (blankIdx) => {
  if (blankIdx == blanks.length) {
    sudoku.forEach((v) => console.log(v.join("")))
    process.exit(0)
  }
  const [r, c] = blanks[blankIdx]

  for (let i = 1; i < 10; i++) {
    const row = rows[r]
    const column = columns[c]
    const square = squares[findSquareIdx(r, c)]
    if (!row[i] && !column[i] && !square[i]) {
      sudoku[r][c] = i
      row[i] = 1
      column[i] = 1
      square[i] = 1
      solve(blankIdx + 1)
      row[i] = 0
      column[i] = 0
      square[i] = 0
      sudoku[r][c] = 0
    }
  }
}
solve(0)