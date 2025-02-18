import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))


Klst = []
aStart = 0
bStart = 0
while aStart < N and bStart < M:
    biggest = 0
    aStartTmp = aStart
    bStartTmp = bStart
    for i in range(aStart, N):
        for j in range(bStart, M):
            if A[i] == B[j] and A[i] > biggest:
                biggest = A[i]
                aStartTmp = i + 1
                bStartTmp = j + 1

    if biggest != 0:
        Klst.append(biggest)
        aStart = aStartTmp
        bStart = bStartTmp
    else:
        break

print(len(Klst))
if Klst:
    print(*Klst)
