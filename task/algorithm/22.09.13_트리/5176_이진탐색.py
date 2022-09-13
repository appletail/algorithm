import sys
sys.stdin = open("input.txt", "r")


# 중위탐색으로 저장
def LVR(k):
    global now
    if 0 < k <= n:
        LVR(k * 2)
        now += 1
        arr[k] = now
        LVR(k * 2 + 1)


for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = [0] * (n + 1)
    now = 0
    LVR(1)
    print(f'#{test_case} {arr[1]} {arr[n // 2]}')