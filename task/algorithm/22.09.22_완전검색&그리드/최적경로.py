import sys
sys.stdin = open("input.txt", "r")


def f(i, k):
    global minV
    if i == k:      # 인덱스 i == 원소의 개수
        tmp = 0
        tmp += abs(se[0][0] - homes[p[0]][0]) + abs(se[0][1] - homes[p[0]][1])
        for m in range(1, n):
            tmp += abs(homes[p[m]][0] - homes[p[m - 1]][0]) + abs(homes[p[m]][1] - homes[p[m - 1]][1])
            if tmp > minV:
                return
        tmp += abs(se[1][0] - homes[p[-1]][0]) + abs(se[1][1] - homes[p[-1]][1])
        minV = min(minV, tmp)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]


T = int(input())
for test_case in range(1, T + 1):

    n = int(input())
    des = list(map(int, input().split()))
    se = [(des[0], des[1]), (des[2], des[3])]
    homes = []
    for i in range(4, (n + 2) * 2, 2):
        homes.append((des[i], des[i + 1]))

    minV = 1e10
    p = [i for i in range(n)]
    f(0, n)

    print(f'#{test_case}', minV)


# 다른 답
# n >> 선택된 원소의 개수, k >> 순열의 길이
def perm(n, k, midSum):
    global minV

    if n == k:
        # 도착했으면 집으로 가기
        midSum += abs(p[n - 1][0] - home[0]) + abs(p[n - 1][1] - home[1])
        if minV > midSum:
            minV = midSum
            return

    else:
        for i in range(n, k):

            p[n], p[i] = p[i], p[n]
            if n >= 1:
                dis = abs(p[n][0] - p[n - 1][0]) + abs(p[n][1] - p[n - 1][1])
                if minV < midSum + dis:
                    p[n], p[i] = p[i], p[n]
                    return
                perm(n + 1, k, midSum + dis)
            else:
                dis = abs(p[n][0] - company[0]) + abs(p[n][1] - company[1])
                if minV < midSum + dis:
                    p[n], p[i] = p[i], p[n]
                    return
                # 첫번째 집으로 갈때는 회사에서 출발하자
                perm(n + 1, k, midSum + dis)

            p[n], p[i] = p[i], p[n]


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    inputV = list(map(int, input().split()))
    p = []
    minV = 999999999999

    company = (inputV[0], inputV[1])
    home = (inputV[2], inputV[3])

    for i in range(4, len(inputV), 2):
        p.append((inputV[i], inputV[i + 1]))

    perm(0, N, 0)
    print(f'#{test_case} {minV}')