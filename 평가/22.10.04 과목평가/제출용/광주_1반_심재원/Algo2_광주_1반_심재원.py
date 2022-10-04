def value(k, curS):    # k: 현재 차수, curS: 보석 가치의 합
    global maxV
    if maxV == M or M < curS:    # 백트래킹(예산을 모두 사용했거나 넘어가는 경우)
        return

    if k == n:    # 모든 원소를 방문한 경우
        maxV = max(maxV, curS)    # 최대값 갱신
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1    # 방문표시
                value(k + 1, curS + jewelry[i])    # 현재 보석가치를 더한 경우
                value(k + 1, curS)    # 현재 보석가치를 안 더한 경우
                visited[i] = 0    # 방문해제


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))

    n = 0    # 새로운 보석 리스트의 수
    jewelry = []    # 조건에 부합하는 보석 리스트
    for i in tmp:
        if i % 4 == 0:
            jewelry.append(i)
        elif i % 6 == 0:
            jewelry.append(i)
        elif i % 7 == 0:
            jewelry.append(i)
        elif i % 9 == 0:
            jewelry.append(i)
        elif i % 11 == 0:
            jewelry.append(i)
        else:
            continue
        n += 1

    maxV = 0    # 결과
    visited = [0] * n    # 부분집합 방문 확인용
    value(0, 0)
    print(f'#{test_case}', maxV)
