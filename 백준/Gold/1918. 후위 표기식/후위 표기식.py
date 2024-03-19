infix = input()
answer = ''
stack = []

for elem in infix:
    if elem.isalpha():
        answer += elem
    else:
        if elem == '(':
            stack.append(elem)
        elif elem == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        elif elem in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                answer += stack.pop()
            stack.append(elem)
        elif elem in ['+', '-']:
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(elem)

while stack:
    answer += stack.pop()

print(answer)
