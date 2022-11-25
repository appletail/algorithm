import sys
import time
starts = time.time()

sys.stdin = open("input.txt", "r")


def binary(page, key):
    start = 1
    end = page
    cnt = 1

    while start <= end:
        mid = int((start + end) / 2)
        if key == mid:
            return cnt
        elif key < mid:
            end = mid
        elif key > mid:
            start = mid
        cnt += 1
    return -1


T = int(input())

for test_case in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    if binary(p, pa) < binary(p, pb):
        win = 'A'
    elif binary(p, pa) > binary(p, pb):
        win = 'B'
    elif binary(p, pa) == binary(p, pb):
        win = 0

    print(f'#{test_case} {win}')

print("time :", time.time() - starts)
