t = int(input())

for j in range(t):
    n = int(input())
    ai = list(map(int, input().split()))

    minV = ai[0]
    maxV = ai[0]
    for i in ai:
        if i > maxV:
            maxV = i
        if i < minV:
            minV = i
    result = maxV - minV

    print(f'#{j + 1} {result}')
