import sys
input = sys.stdin.readline

N = int(input())
xy = [list(map(int, input().split()))  for _ in range(N)]
xy.append(xy[0])

tmp = 0
for i in range(N):
    x1, y1 = xy[i]
    x2, y2 = xy[i+1]
    tmp += x1 * y2 - x2 * y1

print(round(abs(tmp) / 2, 1))
