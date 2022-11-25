import sys
sys.stdin = open("input.txt", "r")


# 후위탐색
def LRV(k):
    if 0 < k <= n + 1:
        L = LRV(c1[k])
        R = LRV(c2[k])
        if node[k].isdecimal():
            return int(node[k])
        elif node[k] == '+':
            return L + R
        elif node[k] == '-':
            return L - R
        elif node[k] == '/':
            return L / R
        elif node[k] == '*':
            return L * R


for test_case in range(1, 11):
    n = int(input())
    node = [0] * (n + 1)
    c1 = [0] * (n + 1)
    c2 = [0] * (n + 1)

    for _ in range(n):
        tmp = list(input().split())
        node[int(tmp[0])] = tmp[1]

        if len(tmp) > 2:
            c1[int(tmp[0])] = int(tmp[2])
            c2[int(tmp[0])] = int(tmp[3])

    print(f'#{test_case} {int(LRV(1))}')
