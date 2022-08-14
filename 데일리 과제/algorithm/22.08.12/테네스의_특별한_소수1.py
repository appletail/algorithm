import sys
sys.stdin = open("input.txt", "r")

# 그때 그때 필요한 만큼만 만드는 경우 중복돼서 더 느림

prime = [False] * 2 + [True] * 999999

def generator(A, B):
    result = []
    for num in range(A, B + 1):
        if prime[num]:
            result.append(num)
            for j in range(num * 2, B + 1, num):
                prime[j] = False

    return result


T = int(input())

for test_case in range(1, T + 1):
    d, a, b = map(int, input().split())

    primes = generator(a, b)

    cnt = 0
    for i in primes:
        if str(d) in str(i):
            cnt += 1

    print(f'#{test_case} {cnt}')


# 미리 소수를 다 만들어 놓는 경우 두배 더 빠름
prime = [False] * 2 + [True] * 999999

for num in range(1000001):
    if prime[num]:
        for j in range(num * 2, 1000001, num):
            prime[j] = False


T = int(input())

for test_case in range(1, T + 1):
    d, a, b = map(int, input().split())

    cnt = 0
    for i in range(a, b + 1):
        if prime[i]:
            if str(d) in str(i):
                cnt += 1

    print(f'#{test_case} {cnt}')
