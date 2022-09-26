def VLR(k):  # 전위 순회
    global cnt
    if k:
        tmp[cnt].append(k)
        cnt += 1
        VLR(c1[k])
        VLR(c2[k])


def LVR(k):  # 중위 순회
    global cnt
    if k:
        LVR(c1[k])
        tmp[cnt].append(k)
        cnt += 1
        LVR(c2[k])


def LRV(k):  # 후위 순회
    global cnt
    if k:
        LRV(c1[k])
        LRV(c2[k])
        tmp[cnt].append(k)
        cnt += 1


def R_LVR(k):  # 정답 중위 순회
    if k:
        R_LVR(c1[k])
        print(max(tmp[k]), end=' ')
        R_LVR(c2[k])


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    c1 = [0] * (N + 1)  # L child
    c2 = [0] * (N + 1)  # R child
    tmp = [[] for _ in range(N + 1)]  # 답 입력

    # 트리 생성
    p_check = 1
    c_check = 1
    for i in range(2, N + 1):
        if c_check == 1:
            c1[p_check] = i
            c_check += 1
        else:
            c2[p_check] = i
            p_check += 1
            c_check = 1

    # 트리 방문 실행
    cnt = 1
    VLR(1)
    cnt = 1
    LVR(1)
    cnt =1
    LRV(1)

    print(f'#{test_case}', end=' ')
    R_LVR(1)
    print()