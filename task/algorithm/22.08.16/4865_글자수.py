import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    str1 = list(set(input()))
    str2 = list(input())

    str_dict = dict()


    for i in str1:
        for j in str2:
            if i == j:
                if i in str_dict:
                    str_dict[i] += 1
                else:
                    str_dict[i] = 1

    maxv = 0
    for i in str_dict.values():
        if maxv < i:
            maxv = i

    print(f'#{test_case} {maxv}')