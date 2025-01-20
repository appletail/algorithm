import sys
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()

stack = []
for cha in string:
    stack.append(cha)
    while True:
        if len(stack) < len(bomb):
            break
        flag = False
        for i in range(len(bomb)):
            if stack[-(i+1)] != bomb[-(i+1)]:
                flag = True
                break
        if flag:
            break
        else:
            for _ in range(len(bomb)):
                stack.pop()

print("".join(stack) if stack else "FRULA")