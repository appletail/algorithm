import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    k = int(input())
    heap_s = []
    heap_l = []
    visited = [0] * 1_000_001
    length, idx = 0, 0
    for _ in range(k):
        order, num = input().rstrip().split()
        if order == 'I':
            num = int(num)
            heappush(heap_s, (num, idx))
            heappush(heap_l, (-num, idx))
            length += 1
            idx += 1
        elif length:
            if num == '1':
                while True:
                    tmp = heappop(heap_l)
                    if not visited[tmp[1]]:
                        visited[tmp[1]] = 1
                        break
            else:
                while True:
                    tmp = heappop(heap_s)
                    if not visited[tmp[1]]:
                        visited[tmp[1]] = 1
                        break
            length -= 1

    if length:
        large, small = 0, 0
        while True:
            tmp = heappop(heap_l)
            if not visited[tmp[1]]:
                large = -tmp[0]
                break
        while True:
            tmp = heappop(heap_s)
            if not visited[tmp[1]]:
                small = tmp[0]
                break
        print(large, small)
    else:
        print('EMPTY')
