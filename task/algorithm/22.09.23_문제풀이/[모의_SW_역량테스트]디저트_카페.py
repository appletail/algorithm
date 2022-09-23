import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    pass




#  교수님 코드
# def solve(k(알아서 응용), r, c, d):
#     if d == 3 and r == stR and c == stC:
#
#         return
#     if r하고 c가 범위를 벗어나거나 같은 디저트면:
#          return
#
#     result[k] = ARR[r][c]
#     newR, newC =
#     solve(k + 1, newR, newC, d)
#     d = (d + 1) % 4
#     newR, newC =
#     solve(k + 1, newR, newC, d)
#
# for r in range(N):
#     for c in range(N):
#         stR, stC = r, c
#         result = [-1] * (4 * N)
#         solve(0, r, c, 0)
