def queen(row, N):
    global answer
    if row == N:
        answer += 1
    else:
        for nCol in range(N):
            flag = True
            for i in range(row):
                if board[i] == nCol:
                    flag = False
                elif row - i == abs(nCol - board[i]):
                    flag = False
                if not flag:
                    break
            if flag:
                board[row] = nCol
                queen(row + 1, N)


N = int(input())
board = [0] * N
answer = 0
queen(0, N)

print(answer)
