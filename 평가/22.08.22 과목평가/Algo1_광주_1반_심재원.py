T = int(input())    # 테스트 케이스 수

for test_case in range(1, T + 1):
    # 입력값
    n = int(input())
    strc_edrc = list(map(int, input().split()))
    ground = [list(map(int, input().split())) for _ in range(n)]

    # 높이의 합
    sumV = 0
    for r in range(strc_edrc[0], strc_edrc[2] + 1):  # 영역의 행
        for c in range(strc_edrc[1], strc_edrc[3] + 1):  # 영역의 열
            sumV += ground[r][c]

    # 영역의 칸 수
    num = (strc_edrc[2] + 1 - strc_edrc[0]) * (strc_edrc[3] + 1 - strc_edrc[1])

    # 평균값
    avg = sumV // num

    # 높이의 평균값으로 평탄화
    result = 0
    for r in range(strc_edrc[0], strc_edrc[2] + 1):  # 영역의 행
        for c in range(strc_edrc[1], strc_edrc[3] + 1):  # 영역의 열
            if ground[r][c] >= avg:  # 높이가 더 큰 경우
                result += ground[r][c] - avg
            else:  # 평균이 더 큰 경우
                result += avg - ground[r][c]

    print(f'#{test_case} {result}')
