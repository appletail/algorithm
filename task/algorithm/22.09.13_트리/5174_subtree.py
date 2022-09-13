import sys
sys.stdin = open("input.txt", "r")


def LVR(k):
    global cnt
    if 0 < k <= e + 2:
        LVR(c1[k])
        cnt += 1
        LVR(c2[k])


for test_case in range(1, int(input()) + 1):
    e, n = map(int, input().split())
    c1 = [0] * (e + 2)
    c2 = [0] * (e + 2)

    lst = list(map(int, input().split()))
    for i in range(0, e * 2, 2):
        if c1[lst[i]] == 0:
            c1[lst[i]] = lst[i + 1]
        else:
            c2[lst[i]] = lst[i + 1]

    cnt = 0
    LVR(n)

    print(f'#{test_case} {cnt}')