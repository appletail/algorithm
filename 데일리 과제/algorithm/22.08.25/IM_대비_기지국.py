import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    board = [list(input()) for _ in range(10)]

    dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for r in range(n):
        for c in range(n):
            if board[r][c] == 'A':
                for dr, dc in dt:
                    nr, nc = r + dr, c + dc
                    if 0 <= r + dr < n and 0 <= c + dc < n and board[r + dr][c + dc] == 'H':
                        board[r + dr][c + dc] = 'X'
            elif board[r][c] == 'B':
                for dr, dc in dt:
                    for distance in range(1, 3):
                        nr, nc = r + dr * distance, c + dc * distance
                        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 'H':
                            board[nr][nc] = 'X'
            elif board[r][c] == 'C':
                for dr, dc in dt:
                    for distance in range(1, 4):
                        nr, nc = r + dr * distance, c + dc * distance
                        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 'H':
                            board[nr][nc] = 'X'

    result = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'H':
                result += 1

    print(f'#{test_case} {result}')
