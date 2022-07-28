# 2557 Hello World
# 주소: https://www.acmicpc.net/problem/2557

# 문제
# Hello World!를 출력하시오.

# 입력
# 없음

# 출력
# Hello World!를 출력하시오.

# 예제 입력 1


# 예제 출력 1


# 제출한 답
# print('Hello World!')

# 알고리즘 분류
# 구현



# 1000 A+B
# 주소: https://www.acmicpc.net/problem/1000

# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 첫째 줄에 A+B를 출력한다.

# 예제 입력 1
# 1 2

# 예제 출력 1
# 3

# 제출한 답
# a, b = map(int, input().split())
# print(a + b)

# 알고리즘 분류
# 수학, 구현, 사칙연산



# 1157 단어 공부
# 주소: https://www.acmicpc.net/problem/1157

# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력1
# Mississipi

# 예제 출력1
# ?

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