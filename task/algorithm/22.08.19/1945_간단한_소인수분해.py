import sys
sys.stdin = open("input.txt", "r")


def soinsu(n):
    abcde = [0, 0, 0, 0, 0]

    while n % 2 == 0:
        abcde[0] += 1
        n //= 2

    while n % 3 == 0:
        abcde[1] += 1
        n //= 3

    while n % 5 == 0:
        abcde[2] += 1
        n //= 5

    while n % 7 == 0:
        abcde[3] += 1
        n //= 7

    while n % 11 == 0:
        abcde[4] += 1
        n //= 11

    return abcde


T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', *soinsu(int(input())))
