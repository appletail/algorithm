N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

answer = [[] for _ in range(N)]
for i in range(N):
    for j in range(K):
        tmp = 0
        for k in range(M):
            tmp += A[i][k] * B[k][j]

        answer[i].append(tmp)

for l in answer:
    print(*l)
