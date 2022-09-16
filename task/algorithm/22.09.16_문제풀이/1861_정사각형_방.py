import sys
sys.stdin = open("input.txt", "r")

# 메모이제이션
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    s, c = 1e10, 0

    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                q = [(row, col)]
                num = arr[row][col]
                cnt = 1
                while q:
                    qr, qc = q.pop()
                    visited[qr][qc] = 1
                    for dr, dc in dt:
                        nr, nc = qr + dr, qc + dc
                        if 0 <= nr < n and 0 <= nc < n and arr[qr][qc] + 1 == arr[nr][nc]:
                            if visited[nr][nc]:
                                cnt += visited[nr][nc]
                                break
                            else:
                               q.append((nr, nc))
                               cnt += 1
                               break

                visited[row][col] = cnt

                if cnt > c:
                    s, c = num, cnt
                elif cnt == c and s > num:
                    s = num

    print(f'#{test_case}', s, c)


# 기존 코드
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    s, c = 1e10, 0

    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                q = [(row, col)]
                num = arr[row][col]
                cnt = 1

                while q:
                    qr, qc = q.pop()
                    visited[qr][qc] = 1
                    for dr, dc in dt:
                        nr, nc = qr + dr, qc + dc
                        if 0 <= nr < n and 0 <= nc < n and arr[qr][qc] + 1 == arr[nr][nc]:
                           q.append((nr, nc))
                           cnt += 1
                           break

                if cnt > c:
                    s, c = num, cnt
                elif cnt == c and s > num:
                    s = num

    print(f'#{test_case}', s, c)






# 다른 답
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
#
# def solution(n):
#     answer = [1000003, 0]
#     nodes = [0 for _ in range(n * n + 1)]
#     counts = [1 for _ in range(n * n + 1)]
#
#     for i in range(n):
#         for j in range(n):
#             nodes[rooms[i][j]] = [i, j]
#
#     for i in range(1, len(nodes)):
#         now = nodes[i]
#
#         if answer[1] < counts[i]:
#             answer = [i - counts[i] + 1, counts[i]]
#         elif answer[1] == counts[i]:
#             answer[0] = min(answer[0], i - counts[i] + 1)
#
#         for j in range(4):
#             x = now[0] + dx[j]
#             y = now[1] + dy[j]
#             if not (0 <= x < n and 0 <= y < n):
#                 continue
#             if i + 1 == rooms[x][y]:
#                 counts[i + 1] += counts[i]
#
#     return answer
#
#
# t = int(input())
# answers = []
#
# for tc in range(1, t + 1):
#     n = int(input())
#     rooms = []
#     for _ in range(n):
#         rooms.append(list(map(int, input().split())))
#
#     result = solution(n)
#     answers.append(f'#{tc} {result[0]} {result[1]}')
#
# for answer in answers:
#     print(answer)