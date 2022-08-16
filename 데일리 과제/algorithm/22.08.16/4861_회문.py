import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    word_lst = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n - m + 1):
            word = ''
            word2 = ''
            for k in range(j, j + m):
                word += word_lst[i][k]
                word2 += word_lst[k][i]

            if word == word[::-1]:
                result = word
            elif word2 == word2[::-1]:
                result = word2

    print(f'#{test_case} {result}')
