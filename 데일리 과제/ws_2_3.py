a = input().lower()
b = input().lower()
c = input().lower()

if (a[-1] == b[0] and b[-1] == c[0]) is True:
    print('Pass')
else:
    print('Fail')