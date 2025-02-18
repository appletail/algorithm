import sys
from math import gcd

input = sys.stdin.readline

def multi(base, power):
    if power == 0:
        return 1

    tmp = multi(base, power // 2)
    if power % 2:
        return tmp * tmp * base % X
    else:
        return tmp * tmp % X

M = int(input())
dices = [list(map(int, input().split())) for _ in range(M)]
X = 1_000_000_007

answer = 0
for n, s in dices:
    cd = gcd(s, n)
    s //= cd
    n //= cd

    answer += s * multi(n, X-2) % X
    
print(answer % X)
