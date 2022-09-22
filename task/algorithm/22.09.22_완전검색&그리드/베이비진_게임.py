import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    baby = list(map(int, input().split()))
    p1, p2 = [], []
    count1 = [0] * 10
    count2 = [0] * 10

    winner = 0
    for i in range(12):
        if i % 2:
            p2.append(baby[i])
            count2[baby[i]] += 1
            if count2[baby[i]] == 3:
                winner = 2
                break
        else:
            p1.append(baby[i])
            count1[baby[i]] += 1
            if count1[baby[i]] == 3:
                winner = 1
                break
        if i >= 6 and i % 2:
            cnt = 0
            for j in range(10):
                if count2[j] > 0:
                    cnt += 1
                    if cnt >= 3:
                        winner = 2
                        break
                else:
                    cnt = 0
            else:
                continue
            break

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