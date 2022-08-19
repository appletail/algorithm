import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    rooms = []
    for _ in range(n):
        rooms += list(map(int, input().split()))

    corridors = [0] * 401

    for i in range(0, n * 2, 2):
        if rooms[i] % 2:  # 홀수에서 시작
            if rooms[i] % 2 == rooms[i + 1] % 2:  # 홀수에서 홀수로
                if rooms[i] < rooms[i + 1]:  # 정방향
                    for j in range(rooms[i], rooms[i + 1] + 2):
                        corridors[j] += 1
                else:  # 역방향
                    for j in range(rooms[i] + 1, rooms[i + 1] - 1, -1):
                        corridors[j] += 1
            elif rooms[i] < rooms[i + 1]:  # 홀수에서 짝수로 정방향
                for j in range(rooms[i], rooms[i + 1] + 1):
                    corridors[j] += 1
            elif rooms[i] > rooms[i + 1]:  # 홀수에서 짝수로 역방향
                for j in range(rooms[i] + 1, rooms[i + 1] - 2, -1):
                    corridors[j] += 1

        else:  # 짝수에서 시작
            if rooms[i] % 2 == rooms[i + 1] % 2:
                if rooms[i] < rooms[i + 1]:
                    for j in range(rooms[i] - 1, rooms[i + 1] + 1):
                        corridors[j] += 1
                else:
                    for j in range(rooms[i], rooms[i + 1] - 2, -1):
                        corridors[j] += 1
            elif rooms[i] < rooms[i + 1]:
                for j in range(rooms[i] - 1, rooms[i + 1] + 2):
                    corridors[j] += 1
            elif rooms[i] > rooms[i + 1]:
                for j in range(rooms[i], rooms[i + 1], -1):
                    corridors[j] += 1

    result = 0

    for c in corridors:
        if c > result:
            result = c

    print(f'#{test_case} {result}')
