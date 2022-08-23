import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    n_lst = list(input().split())

    stack = []
    if n % 2:
        fore = n_lst[0: n//2 + 1]
        rear = n_lst[n//2 + 1: n]
        for i in range(n - (n//2 + 1)):
            stack.append(fore[i])
            stack.append(rear[i])
        stack.append(fore[-1])
    else:
        fore = n_lst[0: n // 2]
        rear = n_lst[n // 2: n]
        for i in range(n//2):
            stack.append(fore[i])
            stack.append(rear[i])


    print(f'#{test_case}', *stack)