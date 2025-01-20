import sys
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))
answer = 0
front = 0
fruitTypes = [0] * 10
fruitTypeCnt = 0

for rear in range(N):
    rearFruit = fruits[rear]
    fruitTypes[rearFruit] += 1
    if fruitTypes[rearFruit] == 1:
        fruitTypeCnt += 1

    while fruitTypeCnt > 2:
        frontFruit = fruits[front]
        fruitTypes[frontFruit] -= 1
        if fruitTypes[frontFruit] == 0:
            fruitTypeCnt -= 1
        front += 1

    answer = max(answer, rear-front+1)

print(answer)
