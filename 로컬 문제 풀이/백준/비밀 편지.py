# TC = int(input())
# for _ in range(TC):
#     message = input()
#     n = int(len(message) ** 0.5)
#     cur = n - 1
#     while cur >= 0:
#         for i in range(cur, len(message), n):
#             print(message[i], end='')
#         cur -= 1
#     print()

import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    message = input()
    n = int(len(message) ** 0.5)
    print(''.join(message[i::n] for i in range(n-1, -1, -1)))