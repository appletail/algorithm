pers = []
grams = []
for i in range(5):
    per_gram = input(f'{i + 1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split()

    if per_gram == ['Done']:
        break
    else:
        pers.append(int(per_gram[0].strip('%')))
        grams.append(int(per_gram[1].strip('gG')))


salts = 0
volume = sum(grams)

per_gram_zip = list(zip(pers, grams))
for salt in per_gram_zip:
    salts += (salt[0] * salt[1]) / 100

result = round((salts / volume) * 100, 2)

print(f'{result}% {round(volume, 2)}g')
