import sys
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
visited = [[0] * M for _ in range(N)]
start = [0, 0]
flag = False

for i in range(N):
    row = input()
    campus.append(row)
    if not flag:
        isI = row.find('I')
        if isI != -1:
            start = [i, isI]
            visited[i][isI] = 1
            flag = True

stack = [start]
answer = 0

while stack:
    r, c = stack.pop()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc] and campus[nr][nc] != 'X':
                visited[nr][nc] = 1
                stack.append([nr, nc])
                if campus[nr][nc] == 'P':
                    answer += 1

print(answer if answer else 'TT')
