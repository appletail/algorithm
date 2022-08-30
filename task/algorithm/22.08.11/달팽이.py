ARR = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
print(ARR)


def selection(value):
    minV = 99999999
    for row in range(N):
        for col in range(N):
            if value < ARR[row][col] < minV:
                minV = ARR[row][col]
                resultR, resultC = row, col

    # resultR, resultC = 0,1

    return resultR, resultC


# 오, 아, 왼, 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
curR, curC = 0, 0

N = 5
check = [[False] * N for _ in range(N)]

d = 0
value = 0
for i in range(N * N):
    (idxR, idxC) = selection(value)
    value = ARR[idxR][idxC]
    ARR[curR][curC], ARR[idxR][idxC] = ARR[idxR][idxC], ARR[curR][curC]
    check[curR][curC] = True
    newR = curR + dr[d]
    newC = curC + dc[d]

    if newR < 0 or newR >= N or newC < 0 or newC >= N or check[newR][newC]:
        d = (d + 1) % 4

    curR = curR + dr[d]
    curC = curC + dc[d]

print(ARR)
