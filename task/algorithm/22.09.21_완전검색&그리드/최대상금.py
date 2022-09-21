import sys
sys.stdin = open("input.txt", "r")


def f(L):
    global maxV
    if L == c:
        tmp = int(''.join(num))
        if maxV < tmp:
            maxV = tmp
    else:
        for i in range(length - 1):
            for j in range(i + 1, length):
                num[i], num[j] = num[j], num[i]
                if tuple(num) not in memo[L]:
                    memo[L].append(tuple(num))
                    f(L + 1)
                num[i], num[j] = num[j], num[i]


T = int(input())
for test_case in range(1, T + 1):
    num, c = input().split()
    num = list(num)
    c = int(c)
    length = len(num)
    memo = [[] for _ in range(10)]
    maxV = 0
    f(0)

    print(f'#{test_case}', maxV)


