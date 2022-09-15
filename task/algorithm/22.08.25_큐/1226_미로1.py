import sys
sys.stdin = open("input.txt", "r")


def maze(arr):
    visited = [[-1] * 16 for _ in range(16)]
    q = []
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 0
                break
        else:
            continue
        break

    dt = [(1, 0), (- 1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.pop(0)
        if arr[r][c] == 3:
            return 1
        for i in dt:
            nr = r + i[0]
            nc = c + i[1]
            if arr[nr][nc] != 1 and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0


for test_case in range(10):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(16)]

    print(f'#{n} {maze(miro)}')
