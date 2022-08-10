import sys
sys.stdin = open("input.txt", "r")

for j in range(10):
    t = int(input())

    num_lst = list(map(int, input().split()))
    result = 0
    for i in range(2, t - 2):
        if max(num_lst[i - 2], num_lst[i - 1], num_lst[i + 1], num_lst[i + 2]) >= num_lst[i]:
            result += 0
        else:
            result += num_lst[i] - max(num_lst[i - 2], num_lst[i - 1], num_lst[i + 1], num_lst[i + 2])

    print(f'#{j + 1} {result}')