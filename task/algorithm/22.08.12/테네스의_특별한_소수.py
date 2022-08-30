import sys
sys.stdin = open("input.txt", "r")

primes = [False] * 1000002


def generation(a, b):
    for num in range(a, b + 1):
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                break
        else:
            primes[num] = True


T = int(input())

for test_case in range(1, T + 1):
    d, a, b = map(int, input().split())
    generation(a, b)
    cnt = 0
    for idx in range(1000000):
        if primes[idx] and str(d) in str(idx):
            cnt += 1
    print(f'#{test_case} {cnt}')