import sys
sys.stdin = open("input.txt", "r")


T = 10

for test_case in range(1, T + 1):
    n = int(input())
    cal = list(input())

    stack = []
    postfix = []

    # 후위표기법
    for i in cal:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    postfix.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == '+' or i == '-':
            if stack and stack[-1] != '(':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(int(i))

    while stack:
        postfix.append(stack.pop())

    # 연산
    for i in postfix:
        if i == '*':
            b = stack.pop()
            a = stack.pop()
            tmp = a * b
            stack.append(tmp)
        elif i == '/':
            b = stack.pop()
            a = stack.pop()
            tmp = a / b
            stack.append(tmp)
        elif i == '+':
            b = stack.pop()
            a = stack.pop()
            tmp = a + b
            stack.append(tmp)
        elif i == '-':
            b = stack.pop()
            a = stack.pop()
            tmp = a - b
            stack.append(tmp)
        else:
            stack.append(i)

    print(f'#{test_case} {stack.pop()}')
