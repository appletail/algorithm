T = int(input())    # 테스트 케이스 수

for test_case in range(1, T + 1):
    # 입력값
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    pat = [list(map(int, input().split())) for _ in range(3)]

    # 모든 3x3을 돌면서 패턴과 비교
    result = 0
    for r in range(n - 2):  # 패턴비교 시작 row
        for c in range(n - 2):  # 패턴비교 시작 col:
            # 패턴 비교
            cnt = 0  # 비교용 카운트
            for i in range(3):  # 행
                for j in range(3):  # 열
                    if arr[r + i][c + j] == pat[i][j]:
                        cnt += 1  # 패턴과 같을 때마다 카운트
                    else:  # 패턴과 다르면 break
                        break
                else:  # 2중 for문 탈출용 else
                    continue
                break
            if cnt == 9:  # 패턴과 일치 여부 확인
                result += 1

    print(f'#{test_case} {result}')
