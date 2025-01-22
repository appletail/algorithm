import sys, copy
input = sys.stdin.readline

def spreadVirus(innerMAP, viruses, blankCnt):
    N, M = len(innerMAP), len(innerMAP[0])
    for vr, vc in viruses:
        stack = [(vr, vc)]
        while stack:
            r, c = stack.pop()
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if innerMAP[nr][nc] == 0:
                        innerMAP[nr][nc] = 2
                        stack.append((nr, nc))
                        blankCnt -= 1

    return blankCnt


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
blank = []
viruses = []
answer = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            blank.append((i, j))
        elif MAP[i][j] == 2:
            viruses.append((i, j))

blankCnt = len(blank)
for i in range(len(blank)-2):
    wall1_r, wall1_c = blank[i]
    MAP[wall1_r][wall1_c] = 1
    blankCnt -= 1
    for j in range(i+1, len(blank)-1):
        wall2_r, wall2_c = blank[j]
        MAP[wall2_r][wall2_c] = 1
        blankCnt -= 1
        for k in range(j+1, len(blank)):
            wall3_r, wall3_c = blank[k]
            MAP[wall3_r][wall3_c] = 1
            blankCnt -= 1
            answer = max(answer, spreadVirus(copy.deepcopy(MAP), viruses, blankCnt))
            MAP[wall3_r][wall3_c] = 0
            blankCnt += 1
        MAP[wall2_r][wall2_c] = 0
        blankCnt += 1
    MAP[wall1_r][wall1_c] = 0
    blankCnt += 1

print(answer)