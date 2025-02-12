def ABmodC(A, B, C):
    if B == 1:
        return A % C

    temp = ABmodC(A, B//2, C)

    if B % 2 == 0:
        return (temp ** 2) % C
    else:
        return ((temp ** 2) * (A % C)) % C

A, B, C = map(int, input().split())

print(ABmodC(A, B, C))
