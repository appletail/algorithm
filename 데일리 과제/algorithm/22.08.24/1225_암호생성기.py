# 1225 암호생성기
# 주소: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=1225&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    n = int(input())

    num_lst = list(map(int, input().split()))

    while num_lst[7] > 0:
        for i in range(5):
            num_lst[0] -= (i + 1)
            if num_lst[0] <= 0:
                num_lst[0] = 0
                num_lst.append(num_lst.pop(0))
                break
            else:
                num_lst.append(num_lst.pop(0))

    print(f'#{n}', *num_lst)


# def encoding(li, k):
#     if k == 6:
#         k = 1
#     if li[0] - k <= 0:
#         li = li[1:] + [0]
#         return li
#     else:
#         return encoding(li[1:] + [li[0] - k], k + 1)
#
#
# for tc in range(10):
#     N = int(input())
#     result = list(map(int, input().split()))
#
#     possible_cycle = min(result) // 15
#     cycle_done = [result[i] - 15 * (possible_cycle - 1) for i in range(len(result))]
#     print("#{} {}".format(N, " ".join(map(str, encoding(cycle_done, 1)))))
