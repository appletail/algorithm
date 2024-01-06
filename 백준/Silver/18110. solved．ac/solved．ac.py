import sys
input = sys.stdin.readline


def roundTraditional(val, digits):
    return int(round(val + 10 ** (-len(str(val)) - 1), digits))


n = int(input())
votes = [int(input()) for _ in range(n)]
votes.sort()

trunc = roundTraditional(n * 0.15, 0)

if n == 0:
    print(0)
else:
    print(roundTraditional(sum(votes[trunc: n - trunc]) / (n - (2 * trunc)), 0))
