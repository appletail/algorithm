import sys
sys.stdin = open("input.txt", "r")


def dfs(sr, sc, w, cnt):
    global result
    if cnt == 7:
        if w not in w_lst:
            w_lst.append(w)
            result += 1
    else:
        for dr, dc in dt:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, w + board[nr][nc], cnt + 1)


T = int(input())
for test_case in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]
    w_lst = []
    dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = 0
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j], 1)

    print(f'#{test_case}', result)


# 다른 답
def dfs(sr, sc, w, cnt):
    if cnt == 7:
        w_lst.append(w)
    else:
        for dr, dc in dt:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, w + board[nr][nc], cnt + 1)


T = int(input())
for test_case in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]
    w_lst = []
    dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j], 1)

    print(f'#{test_case}', len(set(w_lst)))   # set으로 바꿔서 len을 걸면 더 빨라짐...
