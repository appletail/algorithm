# input()
#    - 입력된 값을 문자열로 인식

# 문자열.split(sep='구분자', maxsplit=분할횟수)
#    - 구분자 기준으로 횟수만큼 나누어줌
#    - ()를 비워둘 경우 띄어쓰기나 엔터를 구분자로 하여 문자열을 자름

# input().split()
#    - 입력한 값을 공백을 기준으로 나누어줌

# map(적용할 함수, 반복 가능한 자료형)
#    - 모든 자료형 각각에 함수를 적용



# num = int(input()) 한줄에 문자열을 숫자로 받은 것

# n1, n2 = map(int, input().split())

# print(num)
# print(num, end='')
# print(a + b)


a, b = map(int, input().split())
print(a + b)
