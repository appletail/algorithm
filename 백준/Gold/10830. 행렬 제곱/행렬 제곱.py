import sys
input = sys.stdin.readline

def calculate(matrixA, matrixB):
    n = len(matrixA)
    matrixNew = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += matrixA[i][k] * matrixB[k][j]
            matrixNew[i].append(tmp % 1000)

    return matrixNew

def DnC(matrix, B):
    if B == 1:
        return [list(map(lambda x: x % 1000, matrix[i])) for i in range(len(matrix))]

    temp = DnC(matrix, B//2)
    if B % 2 == 0:
        return calculate(temp, temp)
    else:
        return calculate(calculate(temp, temp), matrix)

N, B = map(int, input().split(" "))
matrix = [list(map(int, input().split(" "))) for _ in range(N)]

answer = DnC(matrix, B)

for row in answer:
    print(*row)
