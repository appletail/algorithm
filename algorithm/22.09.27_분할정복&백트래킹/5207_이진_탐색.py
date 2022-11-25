import sys
sys.stdin = open("input.txt", "r")


def binaryS(k):
    global cnt

    flag = 1
    Lflag, Rflag = 1, 1
    start = 0
    end = n - 1
    e = False

    while start <= end:
        mid = (start + end) // 2
        if k == A[mid]:
            e = True
            break
        elif A[mid] > k:
            end = mid - 1
            if Rflag:
                Lflag, Rflag = 1, 0
            else:
                flag = 0
                break
        else:
            start = mid + 1
            if Lflag:
                Lflag, Rflag = 0, 1
            else:
                flag = 0
                break

    if flag and e:
        cnt += 1


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        binaryS(num)

    print(f'#{test_case}', cnt)
