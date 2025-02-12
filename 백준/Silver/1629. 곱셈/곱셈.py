def ABmodC(A, B, C):
    if B == 1:
        return A % C

    if B % 2 == 0:
        return ((ABmodC(A, B//2, C) % C) ** 2) % C
    else:
        return ((ABmodC(A, B//2, C) % C) ** 2 * (A % C)) % C

A, B, C = map(int, input().split())

print(ABmodC(A, B, C))
