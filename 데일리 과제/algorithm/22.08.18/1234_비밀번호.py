import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    n, moonja = input().split()

    stack = []

    for i in moonja:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    # result = ''
    # for j in stack:
    #     result += j
    result = ''.join(stack) # join 써도 됨

    print(f'#{test_case} {result}')
