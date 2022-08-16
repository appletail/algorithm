import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n_lst = input()

    result = 0
    pipes = 0
    i = 0

    while i < (len(n_lst)):
        if i + 1 < len(n_lst) and n_lst[i] == '(' and n_lst[i + 1] == ')':
            result += pipes
            i += 2
            continue
        if n_lst[i] == '(':
            pipes += 1
        else:
            pipes -= 1
            result += 1
        i += 1


    print(f'#{test_case} {result}')