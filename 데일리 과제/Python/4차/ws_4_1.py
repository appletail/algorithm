password_good = '123456'

for _ in range(3):
    user_password = input('비밀번호를 입력하세요.: ')
    if user_password != password_good:
        print('비밀번호가 틀렸습니다.')
        continue
    print('비밀번호가 맞습니다.')
    break