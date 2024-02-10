import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
trees = [int(input()) for _ in range(N)]

answer = 0
for i in range(1, max(trees) + 1):
    sale = 0
    for tree in trees:
        wood = tree // i
        remain = tree % i
        cost = wood * C
        if not remain:
            cost -= C
        cur_sale = (i * wood * W) - cost
        if cur_sale > 0:
            sale += cur_sale
    answer = max(answer, sale)

print(answer)
