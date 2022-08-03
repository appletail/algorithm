def de_identify(num):
    num = num.replace('-', '')
    result = num[:6] + '*' * 7
    return print(result)

de_identify('970103-1234567')
de_identify('8611232345678')
