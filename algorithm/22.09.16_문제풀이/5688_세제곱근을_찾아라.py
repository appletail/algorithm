import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    a = round(n ** (1/3))
    if a ** 3 == n:
        print(f'#{test_case} {a}')
    else:
        print(f'#{test_case} {-1}')
