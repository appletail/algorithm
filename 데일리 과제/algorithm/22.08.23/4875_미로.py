import sys
sys.stdin = open("input.txt", "r")


def maze():
    global sr
    global sc
    stack = []
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[sr][sc] = True

    while True:
        check = []
        for i in range(4):
            newr = sr + dr[i]
            newc = sc + dc[i]
            if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] != 1 and visited[newr][newc] == False:
                if arr[newr][newc] == 3:
                    return 1
                else:
                    stack.append(i)

        for i in range(4):
            newr = sr + dr[i]
            newc = sc + dc[i]
            if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] != 1 and visited[newr][newc] == False:
                check.append(visited[newr][newc])

        if len(stack) == 0:
            return 0

        if len(check) == 0:
            tmpd = stack.pop()
            sr += dr[tmpd] * -1
            sc += dc[tmpd] * -1
        else:
            tmpd = stack.pop()
            sr += dr[tmpd]
            sc += dc[tmpd]

        visited[sr][sc] = True


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    sr = 0
    sc = 0
    for i in range(n):
        tmp = list(map(int, input()))
        arr.append(tmp)
        if 2 in tmp:
            sr += i
            for j in range(n):
                if tmp[j] == 2:
                    sc += j

    visited = [[False] * n for _ in range(n)]

    print(f'#{test_case} {maze()}')



# 2에서 3까지 갈 수 있으면 1을 return, 아니면 0을 return
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(curR, curC):
    visited = [[False] * N for _ in range(N)]

    ST = []
    # 1. 스택에 시작점을 push, 시작점 방문표시
    ST.append((curR, curC))
    visited[curR][curC] = True
    # 2. 스택에 데이터가 있는 동안
    while ST:
        curR, curC = ST.pop()
        # cur과 연결된 모든 포인트에 대하여
        for d in range(4):
            newR = curR + dr[d]
            newC = curC + dc[d]
            # new가 이동이 가능하면(선이 연결되어 있으면)
            # 방문 안했으면
            if 0 <= newR < N and 0 <= newC < N and MIRO[newR][newC] != 1 and not visited[newR][newC]:
                if MIRO[newR][newC] == 3:
                    return 1
                ST.append((newR, newC))
                visited[newR][newC] = True
    return 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    MIRO = [list(map(int, input())) for _ in range(N)]

    # 2를 찾는다
    for row in range(N):
        if MIRO[row].count(2):
            curC = MIRO[row].index(2)
            curR = row
            break

    print(f'#{test_case} {dfs(curR, curC)}')
