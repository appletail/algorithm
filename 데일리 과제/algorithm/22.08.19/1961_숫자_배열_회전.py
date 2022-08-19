import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    box = [input().split() for _ in range(n)]

    result = [[] for _ in range(n)]

    for i in range(n):
        goo = ''
        ilpal = ''
        isip = ''

        for j in range(n):
            # 90도
            goo += box[n - 1 - j][i]

            # 180도
            ilpal += box[n - 1 - i][n - 1 - j]

            # 270도
            isip += box[j][n - 1 - i]
        result[i].append(goo); result[i].append(ilpal); result[i].append(isip);

    print(f'#{test_case}')
    for k in range(n):
        print(*result[k])


