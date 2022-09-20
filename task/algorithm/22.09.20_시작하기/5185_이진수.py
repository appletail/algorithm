# import sys
# sys.stdin = open("input.txt", "r")

#
# T = int(input())
# for test_case in range(1, T + 1):
#     n, num = input().split()
#
#     result = ''
#     for i in num:
#         if i.isdecimal():
#             c = int(i)
#         else:
#             c = ord(i) - 55
#
#         a = 0b1000
#         for j in range(4):
#             if a & c:
#                 result += '1'
#             else:
#                 result += '0'
#             a >>= 1
#     print(f'#{test_case}', result)
#
#
# # 다른 답
# tc = int(input())
#
# for t in range(1, tc + 1):
#     N, hexa = input().split()
#     hexa = bin(int('0x' + hexa, 16))[2:]
#
#     if len(hexa) % 4:
#         hexa = '0' * (4 - (len(hexa) % 4)) + hexa
#
#     print(f'#{t} {hexa}')
#

# T = int(input())
#
# for test_case in range(1, T + 1):
#     n, num = input().split()
#     result = ''
#     for i in num:
#         result += str('%04d'%int((bin(int('0x' + i, 16))[2:])))
#     print(f'#{test_case}', result)

binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
          '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
          'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

T = int(input())

for test_case in range(1, T + 1):
    n, num = input().split()
    result = ''
    for i in num:
        result += binary.get(i)
    print(f'#{test_case}', result)