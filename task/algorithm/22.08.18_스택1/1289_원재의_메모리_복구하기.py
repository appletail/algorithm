import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    original = input()
    ori_len = len(original)
    init = '0' * ori_len
    a = len(init)

    cnt = 0
    for i in range(ori_len):
        if original[i] != init[i]:
            cnt += 1
            init = init[:i]
            for j in range(ori_len - i):
                init += str(original[i])

    print(f'#{test_case} {cnt}')
