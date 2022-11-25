import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}

    a, b = input().split()

    num_list = input().split()

    for i in num_list:
        num_dict[i] += 1

    print(f'#{test_case}')
    for i in num_dict:
        print((i + ' ') * num_dict[i], end='')
