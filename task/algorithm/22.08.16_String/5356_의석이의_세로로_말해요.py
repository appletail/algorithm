import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n_lst = [input() for _ in range(5)]

    result = ''

    for i in range(15):
        for j in range(5):
            result += n_lst[j][i: i + 1]

    print(f'#{test_case} {result}')

