import sys
sys.stdin = open("input.txt", "r")


def bus(posi, curS):
    global result
    if curS >= result:
        return

    if posi >= n_lst[0]:
        result = min(curS, result)
        return

    for i in range(n_lst[posi], 0, -1):
        bus(posi + i, curS + 1)


T = int(input())
for test_case in range(1, T + 1):
    n_lst = list(map(int, input().split()))
    result = n_lst[0]
    bus(1, -1)
    print(f'#{test_case}', result)


# 다른 답
def moveFunc(pos, cnt):
    global minMov
    if pos >= N - 1:
        if minMov > cnt:
            minMov = cnt
        return
    cnt += 1
    if cnt >= minMov:
        return
    BATTERY = STATION[pos]
    for step in range(BATTERY, 0, -1):
        moveFunc(pos + step, cnt)


T = int(input())

for tc in range(1, T + 1):
    STATION = list(map(int, input().split()))
    N = STATION.pop(0)
    minMov = N
    moveFunc(0, -1)

    print(f"#{tc} {minMov}")




