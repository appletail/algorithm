import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    mock = n // p
    namurgi = n % p

    print(f'#{test_case}', mock ** (p - namurgi) * (mock + 1) ** namurgi)
