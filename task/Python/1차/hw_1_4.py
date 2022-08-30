s = input('숫자를 입력해주세요 : ')
s = list(s)

s = list(map(int, s))

r = sum(s)

print(r)
