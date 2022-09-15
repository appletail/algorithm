import sys

sys.stdin = open("input.txt", "r")


def parent(x, y):
    arr1 = []
    arr2 = []
    for i in [x, y]:
        tmp = i
        while tmp != 1:
            if tmp in c1:
                tmp = c1.index(tmp)
            else:
                tmp = c2.index(tmp)
            if i == x:
                arr1.append(tmp)
            else:
                arr2.append(tmp)

    for i in arr1:
        for j in arr2:
            if i == j:
                return i


def tree(k):
    global cnt

    if 0 < k <= v:
        cnt += 1
        tree(c1[k])
        tree(c2[k])


T = int(input())
for test_case in range(1, T + 1):
    v, e, n1, n2 = map(int, input().split())

    c1 = [0] * (v + 1)
    c2 = [0] * (v + 1)

    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        if c1[lst[i]] == 0:
            c1[lst[i]] = lst[i + 1]
        else:
            c2[lst[i]] = lst[i + 1]

    p = parent(n1, n2)
    cnt = 0
    tree(p)
    print(f'#{test_case} {p} {cnt}')


# 다른 답
tc = int(input())

for t in range(1, tc + 1):
    V, E, a, b = map(int, input().split())
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    parent = [0] * (V + 1)

    arr = list(map(int, input().split()))

    for i in range(0, E * 2, 2):
        if left[arr[i]]:
            right[arr[i]] = arr[i + 1]
        else:
            left[arr[i]] = arr[i + 1]

    for i in range(len(arr) - 1, -1, -2):
        parent[arr[i]] = arr[i - 1]

    s = []
    result = []

    while True:
        if parent[a] in s:
            result.append(parent[a])
            break
        else:
            if parent[a] >= 1:
                s.append(parent[a])
                a = parent[a]

        if parent[b] in s:
            result.append(parent[b])
            break
        else:
            if parent[b] >= 1:
                s.append(parent[b])
                b = parent[b]

    cnt = 0
    q = []
    q.append(result[0])

    while q:
        x = q.pop(0)
        if left[x] != 0:
            q.append(left[x])
            cnt += 1

        if right[x] != 0:
            q.append(right[x])
            cnt += 1

    print(f'#{t} {result[0]} {cnt + 1}')