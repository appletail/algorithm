import sys
sys.stdin = open("input.txt", "r")

code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def search(arr):
    result = ''

    for i in range(n):
        for j in range(m - 55):
            for k in range(j, j + 56, 7):
                if arr[i][k: k + 7] not in code:
                    break
            else:
                result += arr[i][j: j + 56]
                return result


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    barcode = [input() for _ in range(n)]

    password = search(barcode)

    decode = 0  # 다 더한 값
    check_odd = 1  # 홀짝 확인
    odd, even = 0, 0  # 홀짝

    for i in range(0, 56, 7):
        num = code.get(password[i: i + 7])
        decode += num
        if check_odd % 2:
            odd += num
        else:
            even += num
        check_odd += 1

    print(f'#{test_case}', end = ' ')
    if (odd * 3 + even) % 10:
        print(0)
    else:
        print(decode)


# 다른 답
pwDict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    BLANK = '0' * M
    pat = ''
    for _ in range(N):
        row = input()
        if row != BLANK and pat == '':
            pat = row.rstrip('0')[-56:]
            cnt = [0, 0]
            for idx in range(1, 9):
                cnt[idx % 2] += pwDict[pat[7 * (idx - 1):7 * idx]]

    print(f'#{tc}', end=' ')
    if (cnt[1] * 3 + cnt[0]) % 10:
        print(0)
    else:
        print(sum(cnt))