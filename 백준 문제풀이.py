# 2557 Hello World
# 주소: https://www.acmicpc.net/problem/2557

# 제출한 답
# print('Hello World!')



# 1000 A+B
# 주소: https://www.acmicpc.net/problem/1000

# 제출한 답
# a, b = map(int, input().split())
# print(a + b)



# 1157 단어 공부
# 주소: https://www.acmicpc.net/problem/1157

# 제출한 답
# word = input()
# word = word.upper()

# word_dict = {}

# for i in word:
#     if i in word_dict:
#         word_dict[i] += 1
#     else:
#         word_dict[i] = 1

# word_sort = sorted(word_dict.items(), key = lambda x : x[1], reverse = True)

# if len(word_sort) > 1 and word_sort[0][1] == word_sort[1][1]:
#     print('?')
# else:
#     print(word_sort[0][0])

# 다른 답
# st = input().lower()
# dic ={}
# for chr in st:
#     if chr in dic:
#         dic[chr] += 1
#     else:
#         dic[chr] = 1
# listt = [k for k,v in dic.items() if max(dic.values()) == v]  # 리스트 컴프리헨션을 사용하면 모든 맥스값들을 모아준다.

# if len(listt) > 1:
#     print('?')
# else:
#     k=(max(dic, key=dic.get))
#     print(k.upper())



# 2577 숫자의 개수
# 주소: https://www.acmicpc.net/problem/2577

# 제출한 답
# sum_n = 1
# for _ in range(3):
#     num = int(input())
#     sum_n *= num
# sum_n = str(sum_n)

# result_dict = {}
# for i in range(10):
#     result_dict[i] = 0
#     for num in sum_n:
#         if int(num) == i:
#             result_dict[i] += 1
# result_lst = list(result_dict.values())
# for numv in result_lst:
#     print(int(numv))


# 다른 답
# n = str(int(input()) * int(input()) * int(input())) # 다 곱한 뒤 str로 만듦
# for i in '0123456789':                              # 0부터 9까지 차례로 반복
#     print(n.count(i))                               # count를 사용해 갯수 프린트



# 2675 문자열 반복
# 주소: https://www.acmicpc.net/problem/2675

# 제출한 답
# T = int(input())
# for _ in range(T):
#     R, S = input().split()
#     R = int(R)

#     result = ''
#     for word in S:
#         result += word * R
#     print(result)


# 다른 답
# T = int(input())
# for i in range(T):
#   N,S = map(str,input().split())
#   N = int(N)                       # 제출한 답과 동일

#   for i in range(len(S)):
#     print(S[i]*N,end="")           # end=''을 사용해 옆으로 프린트함
#   print()



# 2739 구구단
# 주소: https://www.acmicpc.net/problem/2739

# 제출한 답
# num = int(input())

# for i in range(1, 10):
#     print(f'{num} * {i} = {num * i}')


# 다른 답
# a = int(input())
# for n in range(1,10):
#   print(a, '*', n, '=', a*n)     # f-string 없이 프린트



# 2741 N 찍기
# 주소: https://www.acmicpc.net/problem/2741

# 제출한 답
# n = int(input())
# for i in range(1, n + 1):
#     print(i)



# 2920 음계
# 주소: https://www.acmicpc.net/problem/2920

# 제출한 답
# ascending = list(range(1, 9))
# descending = list(range(8, 0, -1))

# num = list(map(int, input().split()))

# if num == ascending:
#     print('ascending')
# elif num == descending:
#     print('descending')
# else:
#     print('mixed')
 

# 다른 답
# A = list(map(int, input().split()))

# if A == sorted(A):                    # 오름차순과 내림차순을 미리 적어놓을 필요없이
#     print('ascending')                # sorted를 쓰면 된다.
# elif A == sorted(A, reverse=True):
#     print('descending')
# else:
#     print('mixed')



# 8958 OX퀴즈
# 주소: https://www.acmicpc.net/problem/8958

# 제출한 답
# T = int(input())

# for _ in range(T):
#     ox = input()
#     o = 1
#     x = 0
#     result = 0

#     for idx in range(len(ox)):
#         if ox[idx] == 'X':
#             o = 1
#         elif ox[0] == 'O':
#             result += o
#             o += 1
#         elif ox[idx] != ox[idx - 1] and ox[idx] == 'O':
#             result += o
#             o += 1
#         elif ox[idx] == ox[idx - 1] and ox[idx] == 'O':
#             result += o
#             o += 1
#     print(result)


# 다른 답1
# for i in range(int(input())):
#     score = 0
#     premium = 0
#     for ox in input():                      # X면 프리미엄을 0으로 만들고 다음 반복
#         if ox == 'X':                       # O라면 프리미엄에 1을 더한 후 스코어에 더함
#             premium = 0
#             continue
#         premium += 1
#         score += premium
#     print(score)

# 다른 답2
# for i in range(int(input())):
#   score = 0
#   a = list(map(str, input().split('X')))      # X단위로 끊어서 리스트에 저장
#   for j in range(len(a)):                     # 리스트 a의 길이만큼 반복
#     if 'O' in a[j]:                           # X로 시작하는 경우를 위한 if
#       n = len(a[j])                           # n = 인덱스 j번 문자열의 길이
#       score += n*(n+1) / 2                    # 연속한 경우의 점수를 수학적으로 계산
#   print(int(score))



# 10818 최소, 최대
# 주소: https://www.acmicpc.net/problem/10818

# 제출한 답
# N = int(input())

# num_lst = list(map(int, input().split()))
# num_lst.sort()

# print(num_lst[0], num_lst[-1])

# 다른 답
# N = int(input())
# numbers = list(map(int, input().split()))
# print(min(numbers),max(numbers))              # min과 max 사용



# 10869 사칙연산
# 주소: https://www.acmicpc.net/problem/10869

# 제출한 답
# A, B = map(int, input().split())
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)



# 10950 A + B - 3
# 주소: https://www.acmicpc.net/problem/10950

# 제출한 답
# for i in range(int(input())):
#     A, B = map(int, input().split())
#     print(A + B)



# 10951 A + B - 4
# 주소: https://www.acmicpc.net/problem/10951

# 제출한 답
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A + B)
#     except:
#         break



# 10952 A + B - 5
# 주소: https://www.acmicpc.net/problem/10952

# 제출한 답
# while True:
#     A, B = map(int, input().split())
#     if A == 0 and B == 0:
#         break
#     print(A + B)



# 11654 아스키 코드
# 주소: https://www.acmicpc.net/problem/11654

# 제출한 답
# print(ord(input()))


# 11720 숫자의 합
# 주소: https://www.acmicpc.net/problem/11720

# 제출한 답
# N = int(input())

# num = input()

# result = 0
# for i in num:
#     result += int(i)
# print(result)


# 다른 답
# input()
# print(sum(map(int,input())))    # str에 map을 쓰면 글자 하나하나마다 씌워짐



# 2742 기찍 N
# 주소: https://www.acmicpc.net/problem/2742

# 제출한 답
# for i in range(int(input()), 0, -1):
#     print(i)


# 다른 답
# print(*range(int(input()),0,-1))    # asterisk(*)를 씌우면 언패킹이 돼서 5 4 3 2 1 로 출력됨



# 2753 윤년
# 주소: https://www.acmicpc.net/problem/2753

# 제출한 답
# year = int(input())

# if year % 4 == 0 and year % 100 != 0:
#     print(1)
# elif year % 400 == 0:
#     print(1)
# else:
#     print(0)


# 다른 답
# a = int(input())
# print(int(a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)))
# a를 4로 나눈 나머지가 0이고(and) a를 100으로 나눈 나머지가 0이 아닌 경우거나
# a를 4로 나눈 나머지가 0이고(and) a를 400으로 나눈 나머지가 0인 경우
# True가 나오고 이걸 int로 정수로 바꿔주면 1로 나옴
# False인 경우 int로 정수로 바꿔주면 0이 나옴



# 2884 알람 시계
# 주소: https://www.acmicpc.net/problem/2884

# 제출한 답
# H, M = map(int, input().split())

# if H == 0 and M < 45:
#     H = 23
# elif M < 45 and H != 0:
#     H = H - 1

# if M < 45:
#     over_fortyfive = 45 - M
#     M = 60 - over_fortyfive
# else:
#     M = M - 45

# print(H ,M)


# 다른 답
# h, m = map(int, input().split())
# if m >= 45:
#     print(h, m-45)
# else:
#     if h == 0:
#         print(23, m+15)
#     else:
#         print(h-1, m+15)



# 2908 상수
# 주소: https://www.acmicpc.net/problem/2908

# 제출한 답
# A, B = input().split()

# A = A[::-1]
# B = B[::-1]

# print(A if A > B else B)



# 3052 나머지
# 주소: https://www.acmicpc.net/problem/3052

# 제출한 답
# a = set()
# for i in range(10):
#     b = int(input()) % 42
#     a.add(b)
# print(len(a))



# 9498 시험 성적
# 주소: https://www.acmicpc.net/problem/9498

# 제출한 답
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')



# 10171 고양이
# 주소: https://www.acmicpc.net/problem/10171

# 제출한 답
# print("""\    /\\
#  )  ( ')
# (  /  )
#  \(__)|
#  """)



# 10171 개
# 주소: https://www.acmicpc.net/problem/10171

# 제출한 답
# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|''')

# 다른 답
# print(r'''|\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|''')   # r을 쓰면 모양 그대로 프린트 된다.



# 10809 알파벳 찾기
# 주소: https://www.acmicpc.net/problem/10809

# 제출한 답
# word = input()
# for i in range(97, 123):
#     print(word.find(chr(i)), end = ' ')



# 10871 X보다 작은 수
# 주소: https://www.acmicpc.net/problem/10871

# 제출한 답
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# for i in A:
#     if X > i:
#         print(i, end = ' ')



# 10998 AxB
# 주소: https://www.acmicpc.net/problem/10998

# 제출한 답
# A, B = map(int, input().split())
# print(A * B)



# 1085 직사각형에서 탈출
# 주소: https://www.acmicpc.net/problem/1085

# 제출한 답
# x, y, w, h = map(int, input().split())

# garo = x - w
# sero = y - h

# if x <= abs(garo) and x <= abs(sero) and x <= y:
#     print(x)
# elif y <= abs(garo) and y <= abs(sero) and y <= x:
#     print(y)
# elif abs(garo) <= abs(sero) and abs(garo) <= x and abs(garo) <= y:
#     print(abs(garo))

# else:
#     print(abs(sero))

# 다른 답
# x,y,w,h = map(int,input().split() )
# print(min(w-x,h-y,x,y))               # min을 왜 까먹는 걸까?



# 4153 직각삼각형
# 주소: https://www.acmicpc.net/problem/4153

# 제출한 답
# while True:
#     tri = list(map(int, input().split()))
#     if tri == [0, 0, 0]:
#         break
#     tri.sort()
    
#     if tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2:
#         print('right')
#     else:
#         print('wrong')