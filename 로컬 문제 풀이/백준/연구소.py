# 제출한 답 1 - 2416ms / deepcopy 사용

# import sys, copy
# input = sys.stdin.readline
#
# def spreadVirus(innerMAP, viruses, blankCnt):
#     N, M = len(innerMAP), len(innerMAP[0])
#     for vr, vc in viruses:
#         stack = [(vr, vc)]
#         while stack:
#             r, c = stack.pop()
#             for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and 0 <= nc < M:
#                     if innerMAP[nr][nc] == 0:
#                         innerMAP[nr][nc] = 2
#                         stack.append((nr, nc))
#                         blankCnt -= 1
#
#     return blankCnt
#
#
# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# blank = []
# viruses = []
# answer = 0
#
# for i in range(N):
#     for j in range(M):
#         if MAP[i][j] == 0:
#             blank.append((i, j))
#         elif MAP[i][j] == 2:
#             viruses.append((i, j))
#
# blankCnt = len(blank)for i in range(len(blank)-2):
#
#     wall1_r, wall1_c = blank[i]
#     MAP[wall1_r][wall1_c] = 1
#     blankCnt -= 1
#     for j in range(i+1, len(blank)-1):
#         wall2_r, wall2_c = blank[j]
#         MAP[wall2_r][wall2_c] = 1
#         blankCnt -= 1
#         for k in range(j+1, len(blank)):
#             wall3_r, wall3_c = blank[k]
#             MAP[wall3_r][wall3_c] = 1
#             blankCnt -= 1
#             answer = max(answer, spreadVirus(copy.deepcopy(MAP), viruses, blankCnt))
#             MAP[wall3_r][wall3_c] = 0
#             blankCnt += 1
#         MAP[wall2_r][wall2_c] = 0
#         blankCnt += 1
#     MAP[wall1_r][wall1_c] = 0
#     blankCnt += 1
#
# print(answer)

# # 제출한 답 2 - 1732ms / visited 사용
# import sys
# input = sys.stdin.readline
#
# def spreadVirus(MAP, viruses, blankCnt):
#     N, M = len(MAP), len(MAP[0])
#     visited = [[0] * M for _ in range(N)]
#     blankCnt -= 3
#     for vr, vc in viruses:
#         stack = [(vr, vc)]
#         while stack:
#             r, c = stack.pop()
#             for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and 0 <= nc < M:
#                     if MAP[nr][nc] == 0 and not visited[nr][nc]:
#                         visited[nr][nc] = 1
#                         stack.append((nr, nc))
#                         blankCnt -= 1
#
#     return blankCnt
#
#
# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# blank = []
# viruses = []
# answer = 0
#
# for i in range(N):
#     for j in range(M):
#         if MAP[i][j] == 0:
#             blank.append((i, j))
#         elif MAP[i][j] == 2:
#             viruses.append((i, j))
#
# blankCnt = len(blank)
#
# for i in range(blankCnt-2):
#     wall1_r, wall1_c = blank[i]
#     MAP[wall1_r][wall1_c] = 1
#     for j in range(i+1, blankCnt-1):
#         wall2_r, wall2_c = blank[j]
#         MAP[wall2_r][wall2_c] = 1
#         for k in range(j+1, blankCnt):
#             wall3_r, wall3_c = blank[k]
#             MAP[wall3_r][wall3_c] = 1
#             answer = max(answer, spreadVirus(MAP, viruses, blankCnt))
#             MAP[wall3_r][wall3_c] = 0
#         MAP[wall2_r][wall2_c] = 0
#     MAP[wall1_r][wall1_c] = 0
#
# print(answer)


# 제출한 답 3 - 1768ms / visited 사용 + MAP 미수정
# import sys
# input = sys.stdin.readline
#
# def spreadVirus(blankCnt, newWalls):
#     N, M = len(MAP), len(MAP[0])
#     visited = [[0] * M for _ in range(N)]
#     for wallR, wallC in newWalls:
#         visited[wallR][wallC] = 1
#     blankCnt -= 3
#     for vr, vc in viruses:
#         stack = [(vr, vc)]
#         while stack:
#             r, c = stack.pop()
#             for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and 0 <= nc < M:
#                     if MAP[nr][nc] == 0 and not visited[nr][nc]:
#                         visited[nr][nc] = 1
#                         stack.append((nr, nc))
#                         blankCnt -= 1
#
#     return blankCnt
#
#
# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# blank = []
# viruses = []
# answer = 0
#
# for i in range(N):
#     for j in range(M):
#         if MAP[i][j] == 0:
#             blank.append((i, j))
#         elif MAP[i][j] == 2:
#             viruses.append((i, j))
#
# blankCnt = len(blank)
#
# for i in range(blankCnt-2):
#     wall1 = blank[i]
#     for j in range(i+1, blankCnt-1):
#         wall2 = blank[j]
#         for k in range(j+1, blankCnt):
#             wall3 = blank[k]
#             answer = max(answer, spreadVirus(blankCnt, [wall1, wall2, wall3]))
#
# print(answer)


# 제출한 답 4 - 1752ms / stack에 바이러스 모두 투입
# import sys
# input = sys.stdin.readline
#
# def spreadVirus(blankCnt, newWalls):
#     N, M = len(MAP), len(MAP[0])
#     visited = [[0] * M for _ in range(N)]
#     for wallR, wallC in newWalls:
#         visited[wallR][wallC] = 1
#     blankCnt -= 3
#     stack = []
#     for vr, vc in viruses:
#         stack.append((vr, vc))
#
#     while stack:
#         r, c = stack.pop()
#         for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M:
#                 if MAP[nr][nc] == 0 and not visited[nr][nc]:
#                     visited[nr][nc] = 1
#                     stack.append((nr, nc))
#                     blankCnt -= 1
#
#     return blankCnt
#
#
# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# blank = []
# viruses = []
# answer = 0
#
# for i in range(N):
#     for j in range(M):
#         if MAP[i][j] == 0:
#             blank.append((i, j))
#         elif MAP[i][j] == 2:
#             viruses.append((i, j))
#
# blankCnt = len(blank)
#
# for i in range(blankCnt-2):
#     wall1 = blank[i]
#     for j in range(i+1, blankCnt-1):
#         wall2 = blank[j]
#         for k in range(j+1, blankCnt):
#             wall3 = blank[k]
#             answer = max(answer, spreadVirus(blankCnt, [wall1, wall2, wall3]))
#
# print(answer)


# 제출한 답 5 - 1792ms / 함수 안에서 벽 생성 및 벽 해제
# import sys
# input = sys.stdin.readline
#
# def spreadVirus(blankCnt, newWalls):
#     N, M = len(MAP), len(MAP[0])
#     visited = [[0] * M for _ in range(N)]
#     for wallR, wallC in newWalls:
#         MAP[wallR][wallC] = 1
#     blankCnt -= 3
#     stack = []
#     for vr, vc in viruses:
#         stack.append((vr, vc))
#
#     while stack:
#         r, c = stack.pop()
#         for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M:
#                 if MAP[nr][nc] == 0 and not visited[nr][nc]:
#                     visited[nr][nc] = 1
#                     stack.append((nr, nc))
#                     blankCnt -= 1
#     for wallR, wallC in newWalls:
#         MAP[wallR][wallC] = 0
#     return blankCnt
#
#
# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# blank = []
# viruses = []
# answer = 0
#
# for i in range(N):
#     for j in range(M):
#         if MAP[i][j] == 0:
#             blank.append((i, j))
#         elif MAP[i][j] == 2:
#             viruses.append((i, j))
#
# blankCnt = len(blank)
#
# for i in range(blankCnt-2):
#     wall1 = blank[i]
#     for j in range(i+1, blankCnt-1):
#         wall2 = blank[j]
#         for k in range(j+1, blankCnt):
#             wall3 = blank[k]
#             answer = max(answer, spreadVirus(blankCnt, [wall1, wall2, wall3]))
#
# print(answer)

# 제출한 답 6 - 1800ms / 변수 할당 제거
import sys
input = sys.stdin.readline

def spreadVirus(newWalls):
    visited = [[0] * M for _ in range(N)]
    for wallR, wallC in newWalls:
        visited[wallR][wallC] = 1

    cnt = blankCnt - 3
    stack = []
    for vr, vc in viruses:
        stack.append((vr, vc))

    while stack:
        r, c = stack.pop()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if MAP[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))
                    cnt -= 1

    return cnt


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

for i in range(blankCnt-2):
    for j in range(i+1, blankCnt-1):
        for k in range(j+1, blankCnt):
            answer = max(answer, spreadVirus([blank[i], blank[j], blank[k]]))

print(answer)




# 다른 사람 답 - 	1316ms
import sys
from collections import deque


def bfs(tlst):
    # [0] 3개 좌표를 1로 저장 => 벽 막기
    for i, j in tlst:
        arr[i][j] = 1

    # [1] 변수 및 큐 생성, 초기화
    q = deque()
    vv = [[0] * M for _ in range(N)]
    cnt = CNT - 3  # 남은 0의 개수 (max값 찾을 변수)

    for ti, tj in virus:
        q.append((ti, tj))
        vv[ti][tj] = 1

    # [2] 큐에 데이터 있는 동안 한개꺼내서 처리
    while q:
        ci, cj = q.popleft()
        # 네방향, 범위내, 미방문, 조건(==0)
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and vv[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                vv[ni][nj] = 1
                cnt -= 1

    # [-1] 3개 좌표를 0으로 저장 => 벽 해체
    for i, j in tlst:
        arr[i][j] = 0

    return cnt  # 남아있는 0(빈칸) 개수

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# [1] 빈칸 위치, 바이러스 위치를 저장
lst = []
virus = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

CNT = len(lst)
v = [0] * CNT
ans = 0

# [1] 백트레킹으로 풀이
# dfs(0, [])
# print(ans)

# [2] 루프 CNT중에서 3개를 선택 (가능한 모든 조합)
for i in range(CNT - 2):
    for j in range(i + 1, CNT - 1):
        for k in range(j + 1, CNT):
            ans = max(ans, bfs([lst[i], lst[j], lst[k]]))

print(ans)
