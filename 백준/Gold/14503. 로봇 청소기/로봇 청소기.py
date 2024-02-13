import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

clean = [list(map(int, input().split())) for _ in range(n)]
back = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}
direction = {0: (0, -1, 3), 3: (1, 0, 2), 2: (0, 1, 1), 1: (-1, 0, 0)}

cnt = 0
while clean[r][c] != 1:
    # 현위치 청소
    if not clean[r][c]:
        clean[r][c] = 2
        cnt += 1

    # 4방향 청소 안한 곳 확인
    flag = 0
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tr, tc = r + dr, c + dc
        if not clean[tr][tc]:
            flag = 1
            break

    if flag:  # 4방향 중 안한 곳이 있는 경우
        dr, dc, d = direction.get(d)
        nr, nc = r + dr, c + dc
        if not clean[nr][nc]:
            r, c = nr, nc
    else:  # 4방향 막힌 경우
        dr, dc = back.get(d)
        r, c = r + dr, c + dc

print(cnt)
