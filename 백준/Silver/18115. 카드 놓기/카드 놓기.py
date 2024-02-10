import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = deque()

for i in range(1, N + 1):
    skill = A[-i]
    if skill == 1:
        answer.appendleft(i)
    elif skill == 2:
        tmp = answer.popleft()
        answer.appendleft(i)
        answer.appendleft(tmp)
    elif skill == 3:
        answer.append(i)

print(*answer)
