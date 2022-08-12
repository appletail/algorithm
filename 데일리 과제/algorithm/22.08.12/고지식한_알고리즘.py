# 찾으면 패턴의 시작위치를 return 하고
# 못찾으면 -1을 return

def find(arr1, arr2):
    for i in range(N):
        for j in range(M):
            if i < N and j < M and arr1[i] == arr2[j]:
                i += 1
            else:
                break
            if M - 1 == j:
                result = i - M
                return result

    return -1


def find2(t, p):
    i = 0
    j = 0

    while i < N and j < M:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == M:
        return i - M
    else:  # i == N
        return -1



t = 'a pattern matching algorithm'
p = 'rithm'
N = len(t)
M = len(p)
print(find(t, p))
print(find2(t, p))

