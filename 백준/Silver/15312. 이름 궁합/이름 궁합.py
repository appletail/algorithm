A = input()
B = input()

alphaCnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
stack = []
for i in range(len(A)):
    stack.append(alphaCnt[ord(A[i]) - 65])
    stack.append(alphaCnt[ord(B[i]) - 65])

while len(stack) > 2:
    tmp = []
    for i in range(1, len(stack)):
        tmp.append((stack[i]+stack[i-1]) % 10)
    stack = tmp

print(f'{stack[0]}{stack[1]}')
