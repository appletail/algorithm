import sys
sys.stdin = open("input.txt", "r")


direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
change = {1: 2, 2: 1, 3: 4, 4: 3}


T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    micro_lst = [list(map(int, input().split())) for _ in range(k)]

    # 총 반복
    for _ in range(m):
        tmp_dic = {}  # 겹치기 확인용 임시 딕셔너리
        # 각 미생물별 진행
        for micro in micro_lst:
            r, c, m, d = micro
            dr, dc = direction.get(d)
            nr, nc = r + dr, c + dc
            # 끝에 도달했는지 확인
            if nr == 0 or nr == n - 1:
                d = change.get(d)
                m //= 2
            elif nc == 0 or nc == n - 1:
                d = change.get(d)
                m //= 2
            # 좌표 기준으로 딕셔너리에 저장
            if (nr, nc) in tmp_dic:
                tmp_dic[(nr, nc)].append([nr, nc, m, d])
            else:
                tmp_dic[(nr, nc)] = [[nr, nc, m, d]]

        # 새로운 micro_lst 만들기
        micro_lst = []
        for lst in list(tmp_dic.values()):
            nm, nd, max_m = 0, 0, 0
            for micro in lst:
                r, c, m, d = micro
                nm += m
                if m > max_m:
                    max_m, nd = m, d
            if nm:
                micro_lst.append([r, c, nm, nd])

    # 미생물 합 구하기
    result = 0
    for micro in micro_lst:
        result += micro[2]

    print(f'#{test_case} {result}')
