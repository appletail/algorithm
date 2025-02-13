import sys
input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t1 = 0
p1, p2 = 0, 0

for i in sizes:
    t1 += i // T
    t1 += 1 if i % T else 0

print(t1)
print(N//P, N % P)