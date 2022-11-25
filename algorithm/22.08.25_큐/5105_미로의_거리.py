import sys
sys.stdin = open("input.txt", "r")


def maze(arr):
    visited = [[-1] * n for _ in range(n)]
    q = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                q.append((i, j))
                visited[i][j] = 0
                break
        else:
            continue
        break

    dt = [(1, 0), (- 1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.pop(0)
        if arr[r][c] == 2:
            return visited[r][c] - 1
        for i in dt:
            nr = r + i[0]
            nc = c + i[1]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]

    print(f'#{test_case} {maze(miro)}')
