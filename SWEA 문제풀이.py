# 2025 N줄 덧셈
# 주소: https://url.kr/a5i1rt

# [문제]
# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# 단, 주어질 숫자는 10000을 넘지 않는다.


# [예제]
# 주어진 숫자가 10 일 경우 출력해야 할 정답은,
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

# [입력] 
# 10

# [출력] 
# 55


# [제출한 답]
# a = 2
# b = int(input())
# c = 1
# while a <= b:
#     c = c + a
#     a += 1
# print(c)


# [다른 답]
# N = int(input())
 
# sum = 0
# for i in range(1, N+1):
#     sum += i
# print(sum)



# 1936 1대1 가위바위보
# 주소: https://url.kr/v8shyp

# [문제]
# A와 B가 가위바위보를 하였다.
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.


# [입력] 
# 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

# [출력] 
# A가 이기면 A, B가 이기면 B를 출력한다.


# [제출한 답]
# a, b = map(int, input().split())

# if a == 1 and b == 3:
#     print('A')
# elif a == 2 and b == 1:
#     print('A')
# elif a == 3 and b == 2:
#     print('A')
# else:
#     print('B')


# [다른 답]



# 2063 중간값 찾기
# 주소: https://url.kr/wl8amt

# [문제]
# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.


# [예제]
# N이 9 이고, 9개의 점수가 아래와 같이 주어질 경우,
# 85 72 38 80 69 65 68 96 22
# 69이 중간값이 된다.


# [제약 사항]
# 1. N은 항상 홀수로 주어진다.
# 2. N은 9이상 199 이하의 정수이다. (9 ≤ N ≤ 199)


# [입력]
# 입력은 첫 줄에 N 이 주어진다.
# 둘째 줄에 N 개의 점수가 주어진다.


# [출력]
# N 개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.


# [제출한 답]
# N = int(input())
# S = list(map(int, input().split()))
# S.sort()
# N = N // 2

# print(S[N])


# [다른 답]
# n=int(input())
# data=list(map(int,input().split()))
# data.sort()
# result=data[len(data)//2]    => len 함수를 list나 tuple에서 사용하면 그 안에 속한 값의 갯수를 반환함
#                                 그래서 여기서는 n값과 상관없이 list안의 값들의 수를 사용해 문제를 풀어냄
# print(result)



# 2058 자릿수 더하기
# 주소: https://url.kr/5rxw2a

# [문제]
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.


# [제약 사항]
# 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)


# [입력]
# 입력으로 자연수 N이 주어진다.


# [출력]
# 각 자릿수의 합을 출력한다.


# [제출한 답]

# N = int(input())

# a = N // 1000
# b = (N - (a * 1000)) // 100
# c = (N - (a * 1000 + b * 100 )) // 10
# d = N % 10

# print(a + b + c + d)


# [다른 답]

# N = input()           문자열을 이용한 답
#                       input을 쓰면 문자열로 저장되는데
# answer = 0        

# for n in N:           이때 for를 쓰면 각 자릿수의 값이 문자열로 하나씩 출력됨
# 	answer += int(n)    이 문자열을 각각 정수형으로 바꾸고 더하는 방법임
# print(answer)


# N = int(input())      나눗셈을 이용한 답

# answer = 0            N을 10으로 나눈 나머지는 answer에 저장하고
#                       몫은 다시 10으로 나누는 방식
# while(N>0):
#     answer+=(N%10)
#     N=N//10

# print(answer)



# 1989 초심자의 회문검사
# 주소: https://url.kr/pebyaw

# [문제]
# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.


# [제약 사항]
# 각 단어의 길이는 3 이상 10 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# [제출한 답]
# a = int(input())

# for i in range(1, a+1):
#     b = input()
#     c = ''

#     for d in b:
#         c = d + c

#     if b == c:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')


# [다른 답]
# T = int(input())
 
# for test_case in range(1, T + 1):   # #n 을 위한 함수
     
#     text = input()  # 글자적는 칸
#     text_len = len(text)    #글자 수

#     for i in range(text_len//2):            # 가운데 기준으로 절반이 서로 같으면 회문임
#         if text[i] != text[text_len-1-i]:   # text[i]: 글자 앞부터 i번째까지 글자
#             result = 0                      # text[text_len-1-i]: 마지막 글자는 글자 길이에서 1을 뺀 곳임
#                                             # 거기서 하나씩 빼면서 글자 출력
#             break                           # if 만족하면 break하고 result에 0 넣음
#     else:
#         result = 1                          # if 만족 못하고 for끝까지 수행하면 result에 1 넣음
         
#     print(f'#{test_case} {result}')



# 1946 간단한 압축 풀기
# 주소: https://url.kr/bx64md

# [문제]
# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
# 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)
# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

# [예제]
# 압축된 문서의 내용

# A 10
# B 7
# C 5

# 압축을 풀었을 때 원본 문서의 내용

# AAAAAAAAAA
# BBBBBBBCCC
# CC


# [제약사항]
# 1. 압축된 문서의 알파벳과 숫자 쌍의 개수 N은1이상 10이하의 정수이다. (1 ≤ N ≤ 10)
# 2. 주어지는 알파벳 Ci는 A~Z의 대문자이다. (i는 줄의 번호로 1~N까지의 수)
# 3. 알파벳의 연속된 개수로 주어지는 수 Ki는 1이상 20이하의 정수이다. (1 ≤ Ki ≤ 20, i는 줄의 번호로 1~N까지의 수)
# 4. 원본 문서의 너비는 10으로 고정이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1줄까지 Ci와 Ki가 빈 칸을 사이에 두고 주어진다.


# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# [제출한 답]
# a = int(input())

# for i in range(1, a+1):

#     b = int(input())
#     c = ''
#     for mu in range(0, b):
#         d, e = input().split()
#         c += d * int(e)

#     print(f'#{i}')

#     c = list(c)

#     while len(c) > 10:
#         for i in range(0,10):
#             print(c[i],end = '')
#         print()
#         del c[0:10]
#     for i in range(0,len(c)):
#         print(c[i],end = '')
#     print()

# str들을 한 줄에 다 합친다.
# 더한 str을 리스트화한다.
# 리스트 중 0~9까지 프린트한다.
# 리스트에서 삭제하는 코드 0~9를 삭제한다.
# 리스트 갯수가 10미만이 될때까지 반복한다.
# 나머지 리스트를 출력한다.


# [다른 답]
# t = int(input())                                  # t에 테스트 횟수 입력
 
# for tc in range(1, t+1):                          # t만큼 반복   (반복이 끝날 때마다 tc증가)
#     n = int(input())                              # n에 테스트 케이스 횟수
#     document = ''                                 # document에 None 입력
#     for _ in range(n):                            # n만큼 반복
#         Ci, Ki = input().split()                  # Ci와 Ki에 글자와 수 입력
#         document += Ci*int(Ki)                    # document에 글자와 수를 곱한 것들을 더해 한줄의 긴 글을 만듬
         
#     print('#{}'.format(tc))                       # format을 써서 {}에 tc값 대입한 후 print
     
#     for i in range(0, len(document), 10) :        # 0부터 documet의 길이까지 10 단위로 반복
#         print(document[i:i+10])                   # 0~9, 10~19, 20~29 단위로 증가하면서 출력 / list내에 요소 갯수를 넘어가면 남아있는 것 모두 프린트



# 1959. 두 개의 숫자열
# 주소: https://url.kr/bx64md

# [문제]
# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
# 아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
 
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
# 위 예제의 정답은 아래와 같이 30 이 된다.
 

# [제약 사항]
# N 과 M은 3 이상 20 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 두 번째 줄에는 Ai,
# 세 번째 줄에는 Bj 가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# [제출한 답1]

# T = int(input())

# for i in range(1, T + 1):

#     N, M = map(int,input().split())  # N과 M은 range로 사용할 예정
#     Ai = list(map(int, input().split()))
#     Bj = list(map(int, input().split()))

#     if M >= N :
#         a = M - N
#         b = 0
#         d = []
        
#         for j in range(0, a + 1):
#             for k in range(0, N):
#                 c = int(Ai[k]) * (Bj[k + j])
#                 b += c
#             d.append(b)
#             b = 0
#         print(f'#{i} {max(d)}')

#     else:
#         a = N - M
#         b = 0
#         d = []
        
#         for j in range(0, a + 1):
#             for k in range(0, M):
#                 c = int(Bj[k]) * (Ai[k + j])
#                 b += c
#             d.append(b)
#             b = 0
#         print(f'#{i} {max(d)}')


# [제출한 답2]
# T = int(input())

# for i in range(1, T + 1):

#     N, M = map(int,input().split())  # N과 M은 range로 사용할 예정
#     Ai = list(map(int, input().split()))
#     Bj = list(map(int, input().split()))

#     if M < N :
#         M, N = N, M
#         Ai, Bj = Bj, Ai

#     a = M - N
#     b = 0
#     d = []
    
#     for j in range(0, a + 1):
#         for k in range(0, N):
#             c = int(Ai[k]) * (Bj[k + j])
#             b += c
#         d.append(b)
#         b = 0
#     print(f'#{i} {max(d)}')


# [다른 답1]
# T = int(input())
 
# for test_case in range(T):
#     N, M = map(int, input().split())
     
 
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
 
#     result = 0
 
#     if N > M:
#         N, M = M, N
#         A, B = B, A
 
#     for i in range(M-N+1):
#         tmp = 0
#         for j in range(N):
#             tmp += A[j] * B[j+i]
 
#         if tmp > result:
#             result = tmp
 
#     print(f'#{test_case+1} {result}')


# [다른 답2]
# for i in range(int(input())):
#     cnt=0
#     a,b=list(map(int,input().split()))
#     l=list(map(int,input().split()))
#     k=list(map(int,input().split()))
#     if a>b:
#         a,b=b,a
#         l,k=k,l
#     o=0
#     for j in range(b-a+1):
#         p=0
#         for t in range(a):
#             p+=l[t]*k[t+j]
#         if o<p:
#             o=p
#     print(f'#{i+1} {o}')






















