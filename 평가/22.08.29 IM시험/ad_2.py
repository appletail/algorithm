import sys
sys.stdin = open('sample_input.txt', 'r')


def check(cursum, k):
    global result
    if k == ls:
        return cursum
    r, c = start[k]
    for dr, dc in dt:
        arr = board
        sumV = 0
        for dis in range(1, n):
            nr = r + dr * dis
            nc = c + dc * dis
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 1 or arr[nr][nc] == 2:
                    break
                else:
                    arr[nr][nc] = 2
                    sumV += 1
                if nr == 0 or nr == n - 1 or nc == 0 or nc == n - 1:
                    result = min(result, check(cursum + sumV, k + 1))
                    arr = board
    return 1e10


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    start = []
    ls = 0
    for r in range(1, n - 1):
        for c in range(1, n - 1):
            if board[r][c] == 1:
                start.append((r, c))
                ls += 1
    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    st = []
    result = 1e10
    print(check(0, 0))
