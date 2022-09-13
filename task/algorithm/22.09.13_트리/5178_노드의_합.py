import sys
sys.stdin = open("input.txt", "r")


def LRV(l):
    if 1 <= l <= N:
        LRV(l * 2)
        LRV(l * 2 + 1)
        arr[l // 2] += arr[l]


T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a] = b

    LRV(L)
    print(f'#{test_case} {arr[L]}')


# 다른 답
T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())

    TREE = [0 for _ in range(N+1)]
    for m in range(M):
        n, val = map(int, input().split())
        TREE[n] = val

    for n in range(N, L, -1):       # 거꾸로 올라가면서 그 노드에 올려버림
        TREE[n//2] += TREE[n]

    print(f"#{tc+1} {TREE[L]}")
