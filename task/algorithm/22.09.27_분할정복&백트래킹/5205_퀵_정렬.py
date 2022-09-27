import sys
sys.stdin = open("input.txt", "r")


def partitionH(L, R):
    p = L
    i = L + 1
    j = R

    while i <= j:
        while i <= j and a[i] <= a[p]:
            i += 1
        while i <= j and a[j] >= a[p]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[p], a[j] = a[j], a[p]
    return j


def quick_s(L, R):
    if L < R:
        p = partitionH(L, R)
        quick_s(L, p - 1)
        quick_s(p + 1, R)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    quick_s(0, N - 1)
    print(f'#{test_case}', a[N // 2])
    a.sort()