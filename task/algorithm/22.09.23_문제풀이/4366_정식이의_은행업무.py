import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    # 1. 이진수에서 숫자 하나씩만 바꾼것을 set에 넣기
    # 2. 삼진수에서 숫자 하나씩만 바꿔서 set에 넣기
    # 3. set 교집합으로 합치기
    # 4. 합친 것을 출력
    b = list(map(int, input()))
    t = list(map(int, input()))
    lb, lt = len(b), len(t)
    b_set, t_set = set(), set()

    for i in range(lb):
        ori = b[i]
        for j in range(2):
            b[i] = j
            tmp = 0
            for k in range(lb):
                tmp += b[lb - 1 - k] * 2 ** k
            b_set.add(tmp)
            b[i] = ori

    for i in range(lt - 1, -1, -1):
        ori = t[i]
        for j in range(3):
            t[i] = j
            tmp = 0
            for k in range(lt):
                tmp += t[lt - 1 - k] * 3 ** k
            t_set.add(tmp)
            t[i] = ori

    print(f'#{test_case}', *b_set & t_set)
