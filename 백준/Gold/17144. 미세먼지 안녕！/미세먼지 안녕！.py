import sys
input = sys.stdin.readline


def spreadDust(curR, curC):
    spreadedDust = room[curR][curC][0] // 5
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = curR + dr, curC + dc
        if 0 <= nr < R and 0 <= nc < C and room[nr][nc][0] != -1:
            room[curR][curC][0] -= spreadedDust
            room[nr][nc][1] += spreadedDust
            tmp.add((nr, nc))

def workPurifier(r, direction):  # [r, c, -1(상) or 1(하)]
    curR, curC = r, 0
    curR += direction
    room[curR][curC] = [0, 0]
    dusts.discard((curR, curC))

    while 0 < curR < R-1:
        curR += direction
        room[curR-direction][curC] = room[curR][curC]
        dusts.discard((curR, curC))
        if room[curR-direction][curC][0]:
            dusts.add((curR-direction, curC))

    while curC < C-1:
        curC += 1
        room[curR][curC-1] = room[curR][curC]
        dusts.discard((curR, curC))
        if room[curR][curC-1][0]:
            dusts.add((curR, curC-1))

    while curR < r if direction == -1 else r < curR:
        curR -= direction
        room[curR+direction][curC] = room[curR][curC]
        dusts.discard((curR, curC))
        if room[curR+direction][curC][0]:
            dusts.add((curR+direction, curC))

    while curC > 1:
        curC -= 1
        room[curR][curC+1] = room[curR][curC]
        dusts.discard((curR, curC))
        if room[curR][curC+1][0]:
            dusts.add((curR, curC+1))

    room[curR][1] = [0, 0]
    dusts.discard((curR, 1))

R, C, T = map(int, input().split())
room = [list(map(lambda x: [int(x), 0], input().split())) for _ in range(R)]  # [원본 미세먼지, 갱신되는 미세먼지]

machine = []  # [위, 아래]
dusts = set()  # [[위치]]

for r in range(R):
    for c in range(C):
        if room[r][c][0] == -1:
            machine.append(r)
        elif room[r][c][0]:
            dusts.add((r, c))

while T:
    # 미세먼지 확산
    tmp = set()
    for r, c in dusts:
        if not room[r][c][0] // 5:
            continue
        spreadDust(r, c)

    dusts.update(tmp)
    for r, c in dusts:
        room[r][c] = [sum(room[r][c]), 0]

    # 공기청정기 작동
    for idx, r in enumerate(machine):
        if idx == 0:
            workPurifier(r, -1)
        else:
            workPurifier(r, 1)
    T -= 1

answer = 0
for r, c in dusts:
    answer += room[r][c][0]

print(answer)
