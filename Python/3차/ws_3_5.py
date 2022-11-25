salt = 0
salt_vol = 0

for i in range(5):
    per, vol = map(int, input(f'{i + 1}번 소금물: ').split())

    salt += (per * vol) / 100
    salt_vol += vol

salt_per = round(((salt / salt_vol) * 100), 2)

if input('Done 입력: ') == 'Done':
    print(f'{salt_per}, {salt_vol}')