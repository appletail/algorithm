# import sys
# sys.stdin = open("input.txt", "r")


def paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return paper(n - 10) + paper(n - 20) * 2


T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case} {paper(int(input()))}')
