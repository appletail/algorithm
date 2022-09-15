import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    postfix = list(input().split())

    stack = []
    for i in postfix:
        if i == '.':
            result = stack.pop()
        elif i == '+':
            try:
                b = stack.pop()
                a = stack.pop()
                tmp = a + b
                stack.append(tmp)
            except:
                result = 'error'
                break
        elif i == '-':
            try:
                b = stack.pop()
                a = stack.pop()
                tmp = a - b
                stack.append(tmp)
            except:
                result = 'error'
                break
        elif i == '*':
            try:
                b = stack.pop()
                a = stack.pop()
                tmp = a * b
                stack.append(tmp)
            except:
                result = 'error'
                break
        elif i == '/':
            try:
                b = stack.pop()
                a = stack.pop()
                tmp = a // b
                stack.append(tmp)
            except:
                result = 'error'
                break
        else:
            stack.append(int(i))
    if stack:
        result = 'error'

    print(f'#{test_case} {result}')