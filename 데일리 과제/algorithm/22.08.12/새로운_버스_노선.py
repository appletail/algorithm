import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    bus_lst = [list(map(int, input().split())) for _ in range(n)]

    bus_stop = [0] * 1001

    for i in range(n):
        if bus_lst[i][0] != 3: # 일반버스
            for j in range(bus_lst[i][1], bus_lst[i][2] + 1, bus_lst[i][0]):
                bus_stop[j] += 1
        elif bus_lst[i][0] == 3: # 광역급행버스
            if bus_lst[i][1] % 2:   # 홀수일 때
                for j in range(bus_lst[i][1], bus_lst[i][2] + 1):
                    if j % 3 == 0 and j % 10 != 0:
                        bus_stop[j] += 1
            else: # 짝수일 때
                for j in range(bus_lst[i][1], bus_lst[i][2] + 1):
                    if j % 4 == 0:
                        bus_stop[j] += 1

    maxv = 0
    for k in range(1001):
        if bus_stop[k] > maxv:
            maxv = bus_stop[k]

    print(f'#{test_case} {maxv}')




