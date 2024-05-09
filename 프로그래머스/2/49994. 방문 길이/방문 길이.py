def solution(dirs):
    answer = 0
    board = [[{'U': 0, 'D': 0, 'R': 0, 'L': 0} for _ in range(11)] for _ in range(11)]
    move = {'U': [-1, 0, 'D'], 'D': [1, 0, 'U'], 'R': [0, 1, 'L'], 'L': [0, -1, 'R']}
    cur = [5, 5]
    
    for d in dirs:
        r, c = cur
        dr, dc, d_from = move[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < 11 and 0 <= nc < 11:
            if not board[r][c][d]:
                board[r][c][d] = 1
                board[nr][nc][d_from] = 1
                answer += 1
            cur = [nr, nc]
            
    return answer