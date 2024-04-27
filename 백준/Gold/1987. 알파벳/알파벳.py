import sys
input = sys.stdin.readline


def dfs(r, c, cnt):
    maxCnt = cnt
    for nrc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        nr= nrc[0]
        nc = nrc[1]
        if 0 <= nr < R and 0 <= nc < C:
            if not alphabet[ord(board[nr][nc]) - 65]:
                alphabet[ord(board[nr][nc]) - 65] = True
                maxCnt = max(maxCnt, dfs(nr, nc, cnt + 1))
                alphabet[ord(board[nr][nc]) - 65] = False

    return maxCnt

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
alphabet = [0] * 26
alphabet[ord(board[0][0]) - 65] = True
print(dfs(0, 0, 1))
