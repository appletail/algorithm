T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dt = [(1, 0), (-1, 0), (0, 1), (0, -1)]    # 델타

    # 공격 가능 지역 표시
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:    # 방어탑인 경우
                for dr, dc in dt:
                    for d in range(1, N):
                        nr, nc = r + dr * d, c + dc * d    # 델타 X 거리
                        if 0 <= nr < N and 0 <= nc < N:    # 범위 확인
                            if not board[nr][nc]:    # 빈 공간인 경우
                                board[nr][nc] = 3    # 공격 가능 표시
                            elif board[nr][nc] == 1 or board[nr][nc] == 2:    # 장애물이거나 벙어탑인 경우
                                break    # 다음 방향으로

    # 안전지역 개수
    zero = 0
    for r in range(N):
        for c in range(N):
            if not board[r][c]:
                zero += 1

    print(f'#{test_case}', zero)
