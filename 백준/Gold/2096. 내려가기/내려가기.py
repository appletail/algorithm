import sys
input = sys.stdin.readline

N = int(input())

lines = list(map(int, input().split()))
max_lines = [[0] * 3 for _ in range(2)]
min_lines = [[1e10] * 3 for _ in range(2)]

for i in range(3):
    max_lines[0][i], min_lines[0][i] = lines[i], lines[i]

flag = True
read_r, write_r = 0, 1
for _ in range(N - 1):
    lines = list(map(int, input().split()))

    read_r = 0 if flag else 1
    write_r = 1 if flag else 0
    for c in range(3):
        for dc in range(-1, 2):
            nc = c + dc
            if 0 <= nc < 3:
                max_lines[write_r][nc] = max(max_lines[write_r][nc], max_lines[read_r][c] + lines[nc])
                min_lines[write_r][nc] = min(min_lines[write_r][nc], min_lines[read_r][c] + lines[nc])

    for i in range(3):
        max_lines[read_r][i] = 0
        min_lines[read_r][i] = 1e10
    flag = not flag

print_r = read_r if N == 1 else write_r
max_score, min_score = max(max_lines[print_r]), min(min_lines[print_r])

print(max_score, min_score)