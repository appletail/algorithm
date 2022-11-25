# import sys
# sys.stdin = open("input.txt", "r")


def xyzw(n):
    # y 시작 좌표
    result = [0, 0]
    sty = 1
    for i in range(n + 1):
        sty += i
        if n < sty:
            result[1] = i
            break

    # x, y 좌표
    sty -= result[1]
    tmp = n - sty
    result[0] = tmp + 1
    result[1] -= tmp

    return result


T = int(input())

for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    # 좌표
    x, y = xyzw(p)
    z, w = xyzw(q)

    # 새 좌표
    pq = [x + z, y + w]

    result = 1
    for i in range(pq[0] + pq[1] - 1):
        result += i
    result += pq[0] - 1

    print(f'#{test_case}', result)
