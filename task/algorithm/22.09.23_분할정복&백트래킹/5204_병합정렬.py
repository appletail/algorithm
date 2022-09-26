import sys
sys.stdin = open("input.txt", "r")


def merge(lLst, rLst, Llen, Rlen):

    lp = rp = 0
    result = []

    while lp < Llen and rp < Rlen:
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])
            lp += 1
        else:
            result.append(rLst[rp])
            rp += 1

    if rp >= Rlen:
        result += lLst[lp:]
    else:
        result += rLst[rp:]

    return result


def merge_s(lst, length):
    global cnt
    if length == 1:
        return lst
    mid = length // 2
    if length % 2:
        lLen, rLen = mid, mid + 1
    else:
        lLen = rLen = mid

    left = merge_s(lst[:mid], lLen)
    right = merge_s(lst[mid:], rLen)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right, lLen, rLen)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    print(f'#{test_case}', merge_s(nums, N)[N // 2], cnt)
