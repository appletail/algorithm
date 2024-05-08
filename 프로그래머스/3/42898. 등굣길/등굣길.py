def solution(m, n, puddles):
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1] = 1

    for c, r in puddles:
        board[r][c] = -1

    for r in range(1, n+1):
        for c in range(1, m+1):
            if board[r][c] == -1:
                board[r][c] = 0
            else:
                board[r][c] += board[r-1][c] + board[r][c-1]
        
    return board[n][m] % 1_000_000_007