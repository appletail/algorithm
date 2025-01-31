import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

forward = [0] * N
backward = [0] * N
forward[0] = 1
backward[-1] = 1

for i in range(1, N):
    for j in range(i):
        forward[i] = max(forward[i], (forward[j] if A[i] > A[j] else 0) + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        backward[i] = max(backward[i], (backward[j] if A[i] > A[j] else 0) + 1)

answer = 1
for i in range(N):
    answer = max(answer, forward[i]+backward[i])

print(answer-1)
