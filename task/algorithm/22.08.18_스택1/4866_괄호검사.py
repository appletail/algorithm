# import sys
# sys.stdin = open("input.txt", "r")


# T = int(input())
#
# for test_case in range(1, T + 1):
#     check = input()
#     st = []
#
#     for i in check:
#         if i == '{' or i == '(':
#             st.append(i)
#         elif i == '}':
#             if len(st) != 0 and st[-1] == '{':
#                 st.pop()
#             else:
#                 st.append(i)
#                 break
#         elif i == ')':
#             if len(st) != 0 and st[-1] == '(':
#                 st.pop()
#             else:
#                 st.append(i)
#                 break
#
#     if st:
#         result = 0
#     else:
#         result = 1
#
#     print(f'#{test_case} {result}')

T = int(input())

for test_case in range(1, T + 1):
    check = input()
    st = []
    flag = True

    open_it = '{('
    close_it = '})'

    for i in check:
        if i in open_it:
            st.append(i)
        elif i in close_it:
            if len(st) != 0 and open_it.find(st[-1]) == close_it.find(i):
                st.pop()
            else:
                flag = False
                break

    if flag and len(st) == 0:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')