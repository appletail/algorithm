import sys
sys.stdin = open("input.txt", "r")


passcode = {'[3, 2, 1, 1]': '0', '[2, 2, 2, 1]': '1', '[2, 1, 2, 2]': '2', '[1, 4, 1, 1]': '3', '[1, 1, 3, 2]': '4', '[1, 2, 3, 1]': '5', '[1, 1, 1, 4]': '6', '[1, 3, 1, 2]': '7', '[1, 2, 1, 3]': '8', '[3, 1, 1, 2]': '9'}

binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
          '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
          'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    passwords = []
    for i in range(n):
        code = input().strip().rstrip('0')
        if code and not code.isdecimal() and code not in passwords:
            passwords.append(code)

    # 2진수로 변경
    b_passwords = []
    for i in passwords:
        result = ''
        for j in i:
            result += binary.get(j)
        b_passwords.append(result.rstrip('0'))

    arr = []

    for i in range(len(b_passwords)):
        tmp = b_passwords[i]
        while tmp:
            length = len(tmp)
            now, check = 1, 0
            pos = 0
            for j in tmp[::-1]:
                pos += 1
                if now == 1 and j == '0':
                    check += 1
                    now = 0
                elif now == 0 and j == '1':
                    check += 1
                    now = 1
                if check == 4:
                    a = tmp[length - ((pos - 1) * 8):]
                    if a not in arr:
                        arr.append((a, (pos - 1) * 8))
                    tmp = tmp[:length - ((pos - 1) * 8)].rstrip('0')
                    break

    # 숫자로 변경
    answer = []
    for arrary, leng in arr:
        result = ''
        for i in range(0, leng, leng // 8):
            rate = [0, 0, 0, 0]
            now, check = 0, 0
            for j in arrary[i: i + leng // 8]:
                if now == 1 and j == '0':
                    check += 1
                    now = 0
                elif now == 0 and j == '1':
                    check += 1
                    now = 1
                rate[check] += 1

            for k in range(4):
                rate[k] = rate[k] // (leng // 56)
            result += passcode.get(str(rate))
        if result not in answer:
            answer.append(result)

    # 유효성 검사
    result = 0
    for i in answer:
        odd, even = 0, 0
        for j in range(8):
            if j % 2:
                even += int(i[j])
            else:
                odd += int(i[j])
        if not (odd * 3 + even) % 10:
            result += (odd + even)

    print(f'#{test_case}', result)


# 다른 답
pattern = [(2, 1, 1), (2, 2, 1), (1, 2, 2), (4, 1, 1), (1, 3, 2), (2, 3, 1), (1, 1, 4), (3, 1, 2), (2, 1, 3), (1, 1, 2)]
# 첫번째로 나오는 1과 다음에 오는 0, 그리고 다음에 오는 두번 째 연속된 1의 비율을 담은 리스트
# 리스트의 인덱스가 해당 비율을 가지고 있는 암호의 값을 의미

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = sorted(set([input() for _ in range(n)]))[1:]  # 중복 제거 후 맨 앞줄 0인거 제거
    answer = 0  # 최종 결과 값
    joogbok = []  # 같은 암호인지 체크하기 위한 리스트
    for i in arr:
        cnt = 0  # 암호의 길이를 담을 변수
        result = []  # 암호코드 담을 리스트
        fo, fz, so = 0, 0, 0  # 비율 정보 (첫 번째 1의 비율, 다음 첫 번째 0의 비율, 다음 두 번째 1의 비율)
        binary = format(int(i, 16), 'b')  # 16진수 -> 10진수 -> 2진수
        for j in binary:
            j = int(j)
            if j == 1 and not fz:  # 첫 번째 0의 비율에 담긴 값이 한개도 없을 때
                fo += 1
            elif j == 0 and not so and fo:  # 첫 번째 1의 비율에 값이 담겨있고 두 번째 1의 비율에 값이 담겨있지 않을 때
                fz += 1
            elif j == 1 and fz and fo:  # 첫 번째 0의 비율에 값이 담겨 있고 첫 번째 1의 비율에 값이 담겨 있을 때
                so += 1
            elif j == 0 and so:  # 두 번째 1의 비율에 값이 있는데 0이 나올 경우 암호 한글자 완료
                cnt += 1  # 암호 한글자 완료 했으니 암호 길이 +1 (암호 길이가 8이 될 때까지 진행)
                minV = min(fo, fz, so)
                result.append(pattern.index((fo // minV, fz // minV, so // minV)))  # 3개 숫자를 3개 숫자중 최소값으로 나누면 비율이나온다.
                # 그 비율이 무슨 암호를 뜻하는지 알기위해 처음에 저장해놓은 암호 비율 리스트에서 찾아서 해당인덱스를 암호 리스트에 넣는다.
                fo, fz, so = 0, 0, 0  # 암호 한글자 완료 후 비율 값 초기화

            if cnt == 8:  # 암호 8자리를 다 구하면
                if result not in joogbok:  # 전에 구한 암호가 아니면
                    joogbok.append(result)  # 중복 체크용 리스트에 현재 암호를 넣어준다.
                    odd = result[0] + result[2] + result[4] + result[6]
                    even = result[1] + result[3] + result[5]
                    if (odd * 3 + even + result[7]) % 10 == 0:  # 홀수*3 + 짝수 + 마지막숫자(검증 코드) 가 10의 배수이면
                        answer += (odd + even + result[7])  # 최종 결과 값에 암호를 더한 숫자를 더해준다.
                result = []  # 암호 초기화
                cnt = 0  # 암호 길이 초기화

    print(f'#{tc} {answer}')