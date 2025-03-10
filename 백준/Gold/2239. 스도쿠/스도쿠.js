const fs = require("fs")
const filePath = process.platform === "linux" ? "dev/stdin" : "백준/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")

const sudoku = input.map((v) => v.trim().split("").map(Number))

const rows = Array.from(new Array(9), () => new Object())
const columns = Array.from(new Array(9), () => new Object())
const squares = Array.from(new Array(9), () => new Object())
const blanks = []

const findSquareIdx = (i, j) => {
  return Math.floor(i / 3) * 3 + Math.floor(j / 3)
}

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (sudoku[i][j] === 0) blanks.push([i, j])
    else {
      rows[i][sudoku[i][j]] = true
      columns[j][sudoku[i][j]] = true
      squares[findSquareIdx(i, j)][sudoku[i][j]] = true
    }
  }
}

const solve = (blankIdx) => {
  if (blankIdx == blanks.length) return true
  const [r, c] = blanks[blankIdx]

  for (let i = 1; i < 10; i++) {
    const row = rows[r]
    const column = columns[c]
    const square = squares[findSquareIdx(r, c)]
    if (
      !row.hasOwnProperty(i) &&
      !column.hasOwnProperty(i) &&
      !square.hasOwnProperty(i)
    ) {
      sudoku[r][c] = i
      row[i] = true
      column[i] = true
      square[i] = true
      const isDone = solve(blankIdx + 1)
      if (isDone) return true
      delete row[i]
      delete column[i]
      delete square[i]
      sudoku[r][c] = 0
    }
  }
}

solve(0)
sudoku.forEach((v) => console.log(v.join("")))