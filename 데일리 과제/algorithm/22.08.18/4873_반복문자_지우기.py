import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    moonja = list(input())

    while True:
        for i in range(1, len(moonja)):
            if moonja[i - 1] == moonja[i]:
                moonja.pop(i - 1)
                moonja.pop(i - 1)
                break
        else:
            break

    print(f'#{test_case} {len(moonja)}')