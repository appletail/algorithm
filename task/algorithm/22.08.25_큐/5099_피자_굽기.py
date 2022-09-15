import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = []
    idx = 1
    # 남은 피자가 있는 동안
    while pizza:
        # 남은 화덕 공간만큼 피자넣기
        while len(oven) < n:
            oven.append([idx, pizza.pop(0)])
            idx += 1
        # 피자가 다 구워지면 바로 꺼내기
        while pizza:
            if oven[0][1] != 0:
                oven[0][1] //= 2
                if oven[0][1] == 0:
                    oven.pop(0)
                    break
                else:
                    oven.append(oven.pop(0))

    # 나머지 피자 마저 굽기
    while len(oven) != 1:
        if oven[0][1] != 0:
            oven[0][1] //= 2
            if oven[0][1] == 0:
                oven.pop(0)
            else:
                oven.append(oven.pop(0))

    print(f'#{test_case}', oven[0][0])
