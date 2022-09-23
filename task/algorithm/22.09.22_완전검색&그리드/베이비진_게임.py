import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    baby = list(map(int, input().split()))  # 입력
    p1, p2 = [], []     # p1, p2 각 플레이어가 받을 입력
    count1 = [0] * 10   # 각 플레이어의 카드를 카운트
    count2 = [0] * 10

    winner = 0  # 승자 초기화
    for i in range(12):     # 카드를 플레이어 순서에 맞추어 배분
        # 트리플렛 판단
        if i % 2:
            p2.append(baby[i])
            count2[baby[i]] += 1    # 입력 받으며 카드 수 카운트
            if count2[baby[i]] == 3:    # 카운트가 3이 되면 트리플렛으로 판단
                winner = 2  # p2의 승
                break
        else:
            p1.append(baby[i])
            count1[baby[i]] += 1
            if count1[baby[i]] == 3:
                winner = 1
                break

        # 런 판단
        if i >= 6 and i % 2:    # 각각의 플레이어가 받은 카드의 수가 3이상이 되는 경우
            cnt = 0     # 초기화
            for j in range(10):
                if count2[j] > 0:
                    cnt += 1    # 연속한 수가 몇 개인지 확인
                    if cnt >= 3:
                        winner = 2
                        break
                else:       # 연속이 끊기면 0으로 초기화
                    cnt = 0
            else:
                continue    # 이중 포문 탈출을 위한 컨티뉴
            break           # 이중 포문 탈출을 위한 브레이크

        elif i >= 6 and not i % 2:
            cnt = 0
            for j in range(10):
                if count1[j] > 0:
                    cnt += 1
                    if cnt >= 3:
                        winner = 1
                        break
                else:
                    cnt = 0
            else:
                continue
            break

    print(f'#{test_case}', winner)
