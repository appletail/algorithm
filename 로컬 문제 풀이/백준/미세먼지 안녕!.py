import sys
input = sys.stdin.readline

# 제출한 답 - 4952ms
def solution():
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
solution()


# 다른 답 - 1732ms
def solution_other():
    def total_sum(dust):
        total = 0
        for row in dust:
            total += sum(row)
        # 공기청정기 각 -1씩 2가 빠진 것에 대한 2를 더해야함
        return total + 2


    def calc_dust(dust, R, C):
        filter = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        value_update = [[0 for _ in range(C)] for _ in range(R)]
        calculated_dust = [[dust[row][col] // 5 for col in range(C)] for row in range(R)]

        for i in range(R):
            for j in range(C):
                if dust[i][j] == -1:
                    filter.append(i)
                    value_update[i][j] = -1
                    continue

                count = 4  # 각 방향
                add_value = 0

                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if x < 0 or x >= R or y < 0 or y >= C or dust[x][y] == -1:
                        count -= 1
                    else:
                        add_value += calculated_dust[x][y]

                value_update[i][j] = dust[i][j] - (calculated_dust[i][j] * count) + add_value

        return value_update, filter[0], filter[1]


    def start_dust_filter(dust, n, m, R, C):
        # 시계 방향
        for i in range(n - 1, 0, -1):
            dust[i][0] = dust[i - 1][0]
        for i in range(0, C - 1):
            dust[0][i] = dust[0][i + 1]
        for i in range(0, n):
            dust[i][-1] = dust[i + 1][-1]  # dust[i][C - 1] = dust[i + 1][C - 1] 마지막 인덱스 를 수정
        for i in range(C - 1, 0, -1):
            dust[n][i] = dust[n][i - 1]
        dust[n][1] = 0  # 공기청정기가 내보낼 때는 0

        # 반시계 방향
        for i in range(m + 1, R - 1):
            dust[i][0] = dust[i + 1][0]
        for i in range(0, C - 1):
            dust[-1][i] = dust[-1][i + 1]  # dust[R - 1][i] = dust[R - 1][i + 1]
        for i in range(R - 1, m, -1):
            dust[i][-1] = dust[i - 1][-1]  # dust[i][C - 1] = dust[i - 1][C - 1]
        for i in range(C - 1, 1, -1):
            dust[m][i] = dust[m][i - 1]
        dust[m][1] = 0  # 공기청정기가 내보낼 때는 0

        return dust


    R, C, T = map(int, input().split())
    dust = list(list(map(int, input().split())) for _ in range(R))

    for _ in range(T):
        # 계산 후 이동  코드 삽입
        dust, filter_up, filter_down = calc_dust(dust, R, C)
        # 계산 함수 호출
        start_dust_filter(dust, filter_up, filter_down, R, C)

    print(total_sum(dust))

solution_other()