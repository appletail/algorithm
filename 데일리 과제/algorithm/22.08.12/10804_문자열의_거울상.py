T = int(input())

for test_case in range(1, T + 1):
    alpha = input()
    len_alpha = len(alpha) // 2
    alpha = list(alpha)

    for i in range(len_alpha):
        alpha[i], alpha[len(alpha) - 1 - i] = alpha[len(alpha) - 1 - i], alpha[i]

    for i in range(len(alpha)):
        if alpha[i] == 'p':
            alpha[i] = 'q'
        elif alpha[i] == 'q':
            alpha[i] = 'p'
        elif alpha[i] == 'b':
            alpha[i] = 'd'
        else:
            alpha[i] = 'b'

    alpha = ''.join(alpha)

    print(f'#{test_case} {alpha}')
