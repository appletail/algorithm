import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    sequence = list(map(int, input().split()))

    for _ in range(m):
        sequence.append(sequence.pop(0))
    print(f'#{test_case}', sequence[0])
