import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    message = input().strip()
    n = int(len(message) ** 0.5)
    print(''.join(message[i::n] for i in range(n-1, -1, -1)))
    