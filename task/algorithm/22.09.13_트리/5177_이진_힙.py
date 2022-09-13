import sys
sys.stdin = open("input.txt", "r")


def hitit(key):
    global last
    last += 1
    heap[last] = key

    p = last // 2
    c = last
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = p // 2


for test_case in range(1, int(input()) + 1):
    heap = [0] * 501
    last = 0

    n = int(input())
    for i in list(map(int, input().split())):
        hitit(i)

    result = 0
    last //= 2
    while last > 0:
        result += heap[last]
        last //= 2

    print(f'#{test_case} {result}')
