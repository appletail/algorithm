# import sys
# input = sys.stdin.readline
#
# def solution(string, bomb):
#     stack = []
#     for cha in string:
#         stack.append(cha)
#         while True:
#             if len(stack) < len(bomb):
#                 break
#             flag = False
#             for i in range(len(bomb)):
#                 if stack[-(i+1)] != bomb[-(i+1)]:
#                     flag = True
#                     break
#             if flag:
#                 break
#             else:
#                 for _ in range(len(bomb)):
#                     stack.pop()
#
#     return "".join(stack) if stack else "FRULA"


# string = input().strip()
# bomb = input().strip()
# print(solution(string, bomb))


# 다른 풀이
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

# tests = [
#     ['mirkovC4nizCC44', 'C4', 'mirkovniz'],
#     ['12ab112ab2ab', '12ab', 'FRULA'],
# ]
#
# for strings, bomb, result in tests:
#     bomb = list(bomb)
#     answer = solution(strings, bomb)
#     print(answer)
