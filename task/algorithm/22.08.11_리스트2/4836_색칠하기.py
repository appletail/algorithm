import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    colors = [list(map(int, input().split())) for _ in range(n)]

    red = set()
    blue = set()

    for color in colors:
        if color[-1] == 1:
            for r in range(color[0], color[2] + 1):
                for c in range(color[1], color[3] + 1):
                    red.add((r, c))

        elif color[-1] == 2:
            for r in range(color[0], color[2] + 1):
                for c in range(color[1], color[3] + 1):
                    blue.add((r, c))

    result = red & blue

    print(f'#{test_case} {len(result)}')
