import sys
input = sys.stdin.readline

def solution(string, bomb):
    stack = []
    bombLength = len(bomb)
    for cha in string:
        stack.append(cha)
        if stack[-bombLength:] == bomb:
            for _ in range(bombLength):
                stack.pop()

    return "".join(stack) if stack else "FRULA"

string = input().strip()
bomb = list(input().strip())
print(solution(string, bomb))