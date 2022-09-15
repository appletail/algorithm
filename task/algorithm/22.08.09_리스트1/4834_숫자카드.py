import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(t):
    N = int(input())
    num = input()

    card_lst = [0] * 10
    for j in num:
        card_lst[int(j)] += 1

    idx = 0
    maxv = card_lst[0]
    for k in range(10):
        if card_lst[k] >= maxv:
            maxv = card_lst[k]
            idx = k

    print(f'#{i + 1} {idx} {maxv}')