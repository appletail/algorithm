import sys
sys.stdin = open("input.txt", "r")


def maxidx(lst):
    result = lst[0]
    cnt = 0
    for j in lst:
        if j >= result:
            idx = cnt
            result = j
        cnt += 1

    return idx


def minidx(lst):
    result = lst[0]
    cnt = 0
    for j in lst:
        if j <= result:
            idx = cnt
            result = j
        cnt += 1

    return idx


T = 10

for test_case in range(1, T + 1):
    dump = int(input())
    box_lst = list(map(int, input().split()))

    for i in range(dump):
        box_lst[maxidx(box_lst)] -= 1
        box_lst[minidx(box_lst)] += 1

    print(f'#{test_case} {box_lst[maxidx(box_lst)] - box_lst[minidx(box_lst)]}')
